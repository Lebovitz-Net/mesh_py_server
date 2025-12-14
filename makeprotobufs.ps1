#!/usr/bin/env pwsh
mkdir -Force external/protobufs/python
protoc -I=external/protobufs `
  --python_out=external/protobufs/python `
  external/protobufs/meshtastic/*.proto
