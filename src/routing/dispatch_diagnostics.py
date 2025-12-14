# src/routing/dispatch_diagnostics.py

import json
from ..db.insert_handlers import InsertHandlers
from ..meshcore.utils.string_utils import decode_node_info

insert_log_record = InsertHandlers.insertLogRecord
insert_trace_data = InsertHandlers.insertTraceData


class DispatchDiagnostics:
    def log_record_message(self, data: dict, meta: dict):
        conn_id, from_node_num, to_node_num, timestamp = (
            meta.get("connId"),
            meta.get("fromNodeNum"),
            meta.get("toNodeNum"),
            meta.get("timestamp"),
        )

        InsertHandlers.insertLogRecord({
            "message": data.get("message"),
            "time": data.get("time"),
            "fromNodeNum": from_node_num,
            "toNodeNum": to_node_num,
            "timestamp": timestamp,
            "connId": conn_id,
        })

    def handle_LogRxData(self, packet: dict):
        outer_data = packet["data"]
        data = outer_data["data"]
        meta = outer_data["meta"]
        lastSnr, lastRssi = data["lastSnr"], data["lastRssi"]
        print(".../Dispatch rx packet ", lastSnr, lastRssi, meta["timestamp"])
        shaped = {
            "fromNodeNum": 0,
            "decodeType": 0,
            "message": data["raw"].hex(),
            "timestamp": json.dumps({
                "lastSnr": lastSnr,
                "lastRssi": lastRssi,
                "timestamp": meta["timestamp"]
            }),
            "connId": meta["connId"],
        }
        insert_log_record(shaped)

    def handle_TraceData(self, packet: dict):
        outer_data = packet["data"]

        try:
            insert_trace_data(outer_data)
            print("[dispatchDiagnostics] TraceData inserted:",
                  outer_data["data"]["meta"]["connId"])
        except Exception as err:
            print("[dispatchDiagnostics] Failed to insert TraceData:", err)

    def handle_LogRecord(self, sub_packet: dict):
        data, meta = sub_packet["data"], sub_packet["meta"]
        print(".../LogRecord ", sub_packet,
              decode_node_info(data.get("message")))
        self.log_record_message(data, meta)

    def handle_logRecord(self, sub_packet: dict):
        data, meta = sub_packet["data"], sub_packet["meta"]
        print(".../logRecord ", sub_packet)
        self.log_record_message(data, meta)
