from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER,set_ev_cls
from ryu.ofproto import ofproto_v1_3

class StaticRouting(app_manager.RyuApp):
    OFP_Versions=[ofproto_v1_3.OFP_VERSION]
    def add_flow(self,datapath,priority,match,actions):
        ofproto=datapath.ofproto
        parser=datapath.ofproto_parser
        instructions=[ parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,actions)]
        flow_mod=parser.OFPFlowMod(datapath=datapath,priority=priority,match=match,instructions=instructions)
        datapath.send_msg(flow_mod)
    @set_ev_cls(ofp_event.EventOFPSwitchFeatures,CONFIG_DISPATCHER)
    def switch_features_handler(self, ev):
        datapath = ev.msg.datapath
        parser = datapath.ofproto_parser
        dpid = datapath.id
        print("Switch connected:", dpid)

        # switch s1 (dpid = 1)
        if dpid == 1:
            # h1 → s2
            match = parser.OFPMatch(in_port=1)
            actions = [parser.OFPActionOutput(2)]
            self.add_flow(datapath, 1, match, actions)

            # s2 → h1
            match = parser.OFPMatch(in_port=2)
            actions = [parser.OFPActionOutput(1)]
            self.add_flow(datapath, 1, match, actions)

        # switch s2 (dpid = 2)
        elif dpid == 2:
            # s1 → h2
            match = parser.OFPMatch(in_port=1)
            actions = [parser.OFPActionOutput(2)]
            self.add_flow(datapath, 1, match, actions)

            # h2 → s1
            match = parser.OFPMatch(in_port=2)
            actions = [parser.OFPActionOutput(1)]
            self.add_flow(datapath, 1, match, actions)