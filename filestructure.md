# Project File Structure

│—— data
│  ╵—— meshmanager.db
│—— external
│  │—— meshcore_py
│  │  │—— .git
│  │  │  │—— hooks
│  │  │  │  │—— applypatch-msg.sample
│  │  │  │  │—— commit-msg.sample
│  │  │  │  │—— fsmonitor-watchman.sample
│  │  │  │  │—— post-update.sample
│  │  │  │  │—— pre-applypatch.sample
│  │  │  │  │—— pre-commit.sample
│  │  │  │  │—— pre-merge-commit.sample
│  │  │  │  │—— pre-push.sample
│  │  │  │  │—— pre-rebase.sample
│  │  │  │  │—— pre-receive.sample
│  │  │  │  │—— prepare-commit-msg.sample
│  │  │  │  │—— push-to-checkout.sample
│  │  │  │  │—— sendemail-validate.sample
│  │  │  │  ╵—— update.sample
│  │  │  │—— info
│  │  │  │  ╵—— exclude
│  │  │  │—— logs
│  │  │  │  │—— refs
│  │  │  │  │  │—— heads
│  │  │  │  │  │  ╵—— main
│  │  │  │  │  ╵—— remotes
│  │  │  │  │  │  ╵—— origin
│  │  │  │  │  │  │  ╵—— HEAD
│  │  │  │  ╵—— HEAD
│  │  │  │—— objects
│  │  │  │  │—— info
│  │  │  │  ╵—— pack
│  │  │  │  │  │—— pack-59681d98819396a33d92efc8eb992e2490a5e0d2.idx
│  │  │  │  │  │—— pack-59681d98819396a33d92efc8eb992e2490a5e0d2.pack
│  │  │  │  │  ╵—— pack-59681d98819396a33d92efc8eb992e2490a5e0d2.rev
│  │  │  │—— refs
│  │  │  │  │—— heads
│  │  │  │  │  ╵—— main
│  │  │  │  │—— remotes
│  │  │  │  │  ╵—— origin
│  │  │  │  │  │  ╵—— HEAD
│  │  │  │  ╵—— tags
│  │  │  │—— config
│  │  │  │—— description
│  │  │  │—— HEAD
│  │  │  │—— index
│  │  │  ╵—— packed-refs
│  │  │—— src
│  │  │  │—— buffer
│  │  │  │  │—— __pycache__
│  │  │  │  │  │—— buffer_reader.cpython-311.pyc
│  │  │  │  │  ╵—— buffer_writer.cpython-311.pyc
│  │  │  │  │—— buffer_reader.py
│  │  │  │  │—— buffer_utils.py
│  │  │  │  ╵—— buffer_writer.py
│  │  │  │—— connection
│  │  │  │  │—— __pycache__
│  │  │  │  │  │—— connection.cpython-311.pyc
│  │  │  │  │  ╵—— tcp_connection.cpython-311.pyc
│  │  │  │  │—— base_connection_py.txt
│  │  │  │  │—— connection.py
│  │  │  │  │—— py_serial_connection.py
│  │  │  │  │—— serial_connection.py
│  │  │  │  │—— tcp_connection.py
│  │  │  │  │—— web_ble_connection.py
│  │  │  │  ╵—— web_serial_connection.py
│  │  │  │—— __pycache__
│  │  │  │  │—— advert.cpython-311.pyc
│  │  │  │  │—— constants.cpython-311.pyc
│  │  │  │  │—— events.cpython-311.pyc
│  │  │  │  ╵—— packets.cpython-311.pyc
│  │  │  │—— advert.py
│  │  │  │—— cayenne_lpp.py
│  │  │  │—— constants.py
│  │  │  │—— events.py
│  │  │  │—— index.py
│  │  │  │—— packets.py
│  │  │  ╵—— random_utils.py
│  │  │—— LICENSE
│  │  ╵—— README.md
│  ╵—— protobufs
│  │  │—— .git
│  │  │  │—— hooks
│  │  │  │  │—— applypatch-msg.sample
│  │  │  │  │—— commit-msg.sample
│  │  │  │  │—— fsmonitor-watchman.sample
│  │  │  │  │—— post-update.sample
│  │  │  │  │—— pre-applypatch.sample
│  │  │  │  │—— pre-commit.sample
│  │  │  │  │—— pre-merge-commit.sample
│  │  │  │  │—— pre-push.sample
│  │  │  │  │—— pre-rebase.sample
│  │  │  │  │—— pre-receive.sample
│  │  │  │  │—— prepare-commit-msg.sample
│  │  │  │  │—— push-to-checkout.sample
│  │  │  │  │—— sendemail-validate.sample
│  │  │  │  ╵—— update.sample
│  │  │  │—— info
│  │  │  │  ╵—— exclude
│  │  │  │—— logs
│  │  │  │  │—— refs
│  │  │  │  │  │—— heads
│  │  │  │  │  │  ╵—— master
│  │  │  │  │  ╵—— remotes
│  │  │  │  │  │  ╵—— origin
│  │  │  │  │  │  │  │—— eu-433-transitional
│  │  │  │  │  │  │  │—— eu866
│  │  │  │  │  │  │  │—— flat-nodedb
│  │  │  │  │  │  │  │—— HEAD
│  │  │  │  │  │  │  ╵—— master
│  │  │  │  ╵—— HEAD
│  │  │  │—— objects
│  │  │  │  │—— 02
│  │  │  │  │  ╵—— 85198ff77e448a2a6cc43566d322174f8b8450
│  │  │  │  │—— 06
│  │  │  │  │  ╵—— 754c7bcd426e2dbd8e788dbace5dcf31ed2b13
│  │  │  │  │—— 08
│  │  │  │  │  ╵—— bb0fb9a6fd75ddcbdf3665591d845cdaff06d8
│  │  │  │  │—— 09
│  │  │  │  │  ╵—— 9efff59386008736df88f5ce57d3ce0d4dd063
│  │  │  │  │—— 0a
│  │  │  │  │  ╵—— 9bd14ebe283060a6f20af0d24de5aa28a12b48
│  │  │  │  │—— 18
│  │  │  │  │  ╵—— e8eb1c6443717dd02dfd44590387f274f4a063
│  │  │  │  │—— 1e
│  │  │  │  │  ╵—— b869b7a9a6ca1288b66b28981d57d56e2006dc
│  │  │  │  │—— 1f
│  │  │  │  │  ╵—— 12fbfe69a42e1fa0e3050a335369cef764c267
│  │  │  │  │—— 21
│  │  │  │  │  ╵—— b63292e05ea60f87c9642ef256ae9bbbd31fde
│  │  │  │  │—— 23
│  │  │  │  │  ╵—— 2d34f8594def1ae8c41fe3d1cd0fe9587fa6ff
│  │  │  │  │—— 29
│  │  │  │  │  ╵—— c5f6efdcb3c5f7b1c3e75ae7ad74c3d4cb6386
│  │  │  │  │—— 38
│  │  │  │  │  ╵—— d066501125b37d866cd01ea7d97c3ef6909041
│  │  │  │  │—— 3d
│  │  │  │  │  ╵—— 97750ba68dae573a4d342881df907a337e447f
│  │  │  │  │—— 40
│  │  │  │  │  ╵—— 4532984c5a30306845aee8192bd652d99549aa
│  │  │  │  │—— 52
│  │  │  │  │  ╵—— fa252f1e01be87ad2f7ab17ceef7882b2a4a93
│  │  │  │  │—— 60
│  │  │  │  │  ╵—— f9ce37dfbd3f2886ed3f5e1df359e7e36004c0
│  │  │  │  │—— 61
│  │  │  │  │  ╵—— e1180e042f45eb3ec4405e3dce5015ec38bff3
│  │  │  │  │—— 68
│  │  │  │  │  ╵—— dee221b201e99b3124be85953c834ade6f7cc1
│  │  │  │  │—— 6a
│  │  │  │  │  ╵—— 06407e22ee5a350e74a4e48bef2670e3785259
│  │  │  │  │—— 6b
│  │  │  │  │  ╵—— 4d6d6c24af624002b3c630ce874f13b0551cff
│  │  │  │  │—— 6f
│  │  │  │  │  │—— 3845de77a25c3ac8c559238cfe26ef37d18f0b
│  │  │  │  │  ╵—— 9af0365b232856c3570635a0d6ced88775ae8d
│  │  │  │  │—— 71
│  │  │  │  │  ╵—— d50833c81fbd148735f3c9990c837183cbc717
│  │  │  │  │—— 72
│  │  │  │  │  ╵—— ddff74db875acf4bd532a23706a225896ef0f9
│  │  │  │  │—— 76
│  │  │  │  │  ╵—— 54db2e2d1834aebde40090a9b74162ad1048ae
│  │  │  │  │—— 77
│  │  │  │  │  ╵—— 4c5e9f216ab48c2253c46426ea2a2337a05f97
│  │  │  │  │—— 7b
│  │  │  │  │  ╵—— f611e8919514c1c895d9850498fe44ab2c18f0
│  │  │  │  │—— 7d
│  │  │  │  │  ╵—— 6294dd717ad966c247c00d78bc339b1da61752
│  │  │  │  │—— 7e
│  │  │  │  │  ╵—— b3258fa06d7c5e5a32564b4c5b38326640c796
│  │  │  │  │—— 83
│  │  │  │  │  ╵—— ddaf8b24e1e9b372b1e2c72df51d44848b3a71
│  │  │  │  │—— 84
│  │  │  │  │  ╵—— a8db6db87e8a0c723c5882d95602e5cdba4718
│  │  │  │  │—— 89
│  │  │  │  │  ╵—— c9d965479b71b7a72e52579e56fb116ba6982d
│  │  │  │  │—— 9a
│  │  │  │  │  ╵—— db17d940c236625ab0bcf6fb3c4c6ddfc695e9
│  │  │  │  │—— 9d
│  │  │  │  │  ╵—— befbd9002e8010a2b4df65389d3dcc98d76ff4
│  │  │  │  │—— a3
│  │  │  │  │  ╵—— 4428168df5751a1729c2b11f8191a62cdc5009
│  │  │  │  │—— a9
│  │  │  │  │  ╵—— 16c49299cd3739a33a8c08bfbbc8248b51476d
│  │  │  │  │—— b2
│  │  │  │  │  ╵—— 9d09f9e6689085bac9876ff29f7940676c9aad
│  │  │  │  │—— b6
│  │  │  │  │  ╵—— f8f67e5b4053db14b3932211f0fc7098199fb0
│  │  │  │  │—— b9
│  │  │  │  │  ╵—— 6a63d6fe535a400521e066c6d05121ea2c7c60
│  │  │  │  │—— ba
│  │  │  │  │  ╵—— 24df9ab39ca9cb26ae5daf66225280cbc9236c
│  │  │  │  │—— bc
│  │  │  │  │  │—— a435578774b2347e1d81fc267bc7777e874ba9
│  │  │  │  │  ╵—— c0f0119540edaff012257d683434b64ad8f773
│  │  │  │  │—— c4
│  │  │  │  │  ╵—— df45d75ca3d8aea7c19fdf519825a14cdfa0db
│  │  │  │  │—— cd
│  │  │  │  │  ╵—— 4b81cf07901c2e8d730f0481e4f1d8a0b2b5bb
│  │  │  │  │—— cf
│  │  │  │  │  ╵—— 7b18652c3d5521cf46f8b0c2fdf1bea456e1c6
│  │  │  │  │—— e1
│  │  │  │  │  ╵—— b5aaedff3c06cbaf59008c2e744a3421b11c08
│  │  │  │  │—— e5
│  │  │  │  │  ╵—— f722c3755d12f867b7ccdb2036015a06d51318
│  │  │  │  │—— ec
│  │  │  │  │  ╵—— 9d94118159f00c22de2cddf0349533b5cf4f18
│  │  │  │  │—— f6
│  │  │  │  │  ╵—— 1e4e0090b405d2591bfb9ea649ae6505d63cce
│  │  │  │  │—— f9
│  │  │  │  │  ╵—— 38c50ea42b55a4d54c66bf096ec415700e3dc1
│  │  │  │  │—— fb
│  │  │  │  │  ╵—— e1538c21f87e6717e6617ac21bc0799e594ec7
│  │  │  │  │—— fd
│  │  │  │  │  ╵—— 222ae15360d1781cc382ad112b32685a7a4a05
│  │  │  │  │—— info
│  │  │  │  ╵—— pack
│  │  │  │  │  │—— pack-f299598379725f0f616fd7d68641a6580f7a90b6.idx
│  │  │  │  │  │—— pack-f299598379725f0f616fd7d68641a6580f7a90b6.pack
│  │  │  │  │  ╵—— pack-f299598379725f0f616fd7d68641a6580f7a90b6.rev
│  │  │  │—— refs
│  │  │  │  │—— heads
│  │  │  │  │  ╵—— master
│  │  │  │  │—— remotes
│  │  │  │  │  ╵—— origin
│  │  │  │  │  │  │—— eu-433-transitional
│  │  │  │  │  │  │—— eu866
│  │  │  │  │  │  │—— flat-nodedb
│  │  │  │  │  │  │—— HEAD
│  │  │  │  │  │  ╵—— master
│  │  │  │  ╵—— tags
│  │  │  │  │  │—— v2.7.13
│  │  │  │  │  │—— v2.7.14
│  │  │  │  │  │—— v2.7.15
│  │  │  │  │  ╵—— v2.7.16
│  │  │  │—— config
│  │  │  │—— description
│  │  │  │—— FETCH_HEAD
│  │  │  │—— HEAD
│  │  │  │—— index
│  │  │  │—— ORIG_HEAD
│  │  │  ╵—— packed-refs
│  │  │—— .github
│  │  │  │—— workflows
│  │  │  │  │—— ci.yml
│  │  │  │  │—— create_tag.yml
│  │  │  │  │—— publish.yml
│  │  │  │  ╵—— pull_request.yml
│  │  │  ╵—— pull_request_template.md
│  │  │—— .vscode
│  │  │  │—— extensions.json
│  │  │  ╵—— settings.json
│  │  │—— meshtastic
│  │  │  │—— admin.options
│  │  │  │—— admin.proto
│  │  │  │—— apponly.options
│  │  │  │—— apponly.proto
│  │  │  │—— atak.options
│  │  │  │—— atak.proto
│  │  │  │—— cannedmessages.options
│  │  │  │—— cannedmessages.proto
│  │  │  │—— channel.options
│  │  │  │—— channel.proto
│  │  │  │—— clientonly.options
│  │  │  │—— clientonly.proto
│  │  │  │—— config.options
│  │  │  │—— config.proto
│  │  │  │—— connection_status.options
│  │  │  │—— connection_status.proto
│  │  │  │—— deviceonly.options
│  │  │  │—— deviceonly.proto
│  │  │  │—— device_ui.options
│  │  │  │—— device_ui.proto
│  │  │  │—— interdevice.options
│  │  │  │—— interdevice.proto
│  │  │  │—— localonly.proto
│  │  │  │—— mesh.options
│  │  │  │—— mesh.proto
│  │  │  │—— module_config.options
│  │  │  │—— module_config.proto
│  │  │  │—— mqtt.options
│  │  │  │—— mqtt.proto
│  │  │  │—— paxcount.proto
│  │  │  │—— portnums.proto
│  │  │  │—— powermon.proto
│  │  │  │—— remote_hardware.proto
│  │  │  │—— rtttl.options
│  │  │  │—— rtttl.proto
│  │  │  │—— storeforward.options
│  │  │  │—— storeforward.proto
│  │  │  │—— telemetry.options
│  │  │  │—— telemetry.proto
│  │  │  │—— xmodem.options
│  │  │  ╵—— xmodem.proto
│  │  │—— packages
│  │  │  │—— rust
│  │  │  │  │—— src
│  │  │  │  │  │—— generated
│  │  │  │  │  │  ╵—— .gitkeep
│  │  │  │  │  ╵—— lib.rs
│  │  │  │  │—— Cargo.lock
│  │  │  │  ╵—— Cargo.toml
│  │  │  ╵—— ts
│  │  │  │  │—— lib
│  │  │  │  │  ╵—— .gitkeep
│  │  │  │  │—— deno.json
│  │  │  │  │—— deno.lock
│  │  │  │  │—— mod.ts
│  │  │  │  ╵—— package.json
│  │  │—— python
│  │  │  ╵—— meshtastic
│  │  │  │  │—— __pycache__
│  │  │  │  │  ╵—— mesh_pb2.cpython-311.pyc
│  │  │  │  │—— admin_pb2.py
│  │  │  │  │—— apponly_pb2.py
│  │  │  │  │—— atak_pb2.py
│  │  │  │  │—— cannedmessages_pb2.py
│  │  │  │  │—— channel_pb2.py
│  │  │  │  │—— clientonly_pb2.py
│  │  │  │  │—— config_pb2.py
│  │  │  │  │—— connection_status_pb2.py
│  │  │  │  │—— deviceonly_pb2.py
│  │  │  │  │—— device_ui_pb2.py
│  │  │  │  │—— interdevice_pb2.py
│  │  │  │  │—— localonly_pb2.py
│  │  │  │  │—— mesh_pb2.py
│  │  │  │  │—— module_config_pb2.py
│  │  │  │  │—— mqtt_pb2.py
│  │  │  │  │—— paxcount_pb2.py
│  │  │  │  │—— portnums_pb2.py
│  │  │  │  │—— powermon_pb2.py
│  │  │  │  │—— remote_hardware_pb2.py
│  │  │  │  │—— rtttl_pb2.py
│  │  │  │  │—— storeforward_pb2.py
│  │  │  │  │—— telemetry_pb2.py
│  │  │  │  ╵—— xmodem_pb2.py
│  │  │—— .gitattributes
│  │  │—— .gitignore
│  │  │—— buf.gen.yaml
│  │  │—— buf.yaml
│  │  │—— LICENSE
│  │  │—— nanopb.proto
│  │  │—— README.md
│  │  ╵—— renovate.json
│—— src
│  │—— api
│  │  │—— __pycache__
│  │  │  │—— api_utils.cpython-311.pyc
│  │  │  │—— config_handlers.cpython-311.pyc
│  │  │  │—— contacts_handlers.cpython-311.pyc
│  │  │  │—— control_handlers.cpython-311.pyc
│  │  │  │—— devices_handlers.cpython-311.pyc
│  │  │  │—— diagnostics_handlers.cpython-311.pyc
│  │  │  │—— global_state.cpython-311.pyc
│  │  │  │—— handlers.cpython-311.pyc
│  │  │  │—— messages_handlers.cpython-311.pyc
│  │  │  │—— metrics_handlers.cpython-311.pyc
│  │  │  │—— nodes_handlers.cpython-311.pyc
│  │  │  │—— routes.cpython-311.pyc
│  │  │  │—— runtime_config_routes.cpython-311.pyc
│  │  │  │—— services_manager.cpython-311.pyc
│  │  │  ╵—— system_handlers.cpython-311.pyc
│  │  │—— api_utils.py
│  │  │—— config_handlers.py
│  │  │—— contacts_handlers.py
│  │  │—— control_handlers.py
│  │  │—— devices_handlers.py
│  │  │—— diagnostics_handlers.py
│  │  │—— global_state.py
│  │  │—— handlers.py
│  │  │—— messages_handlers.py
│  │  │—— metrics_handlers.py
│  │  │—— nodes_handlers.py
│  │  │—— routes.py
│  │  │—— runtime_config_routes.py
│  │  │—— services_manager.py
│  │  ╵—— system_handlers.py
│  │—— config
│  │  │—— __pycache__
│  │  │  │—— config.cpython-311.pyc
│  │  │  ╵—— __init__.cpython-311.pyc
│  │  │—— config.py
│  │  ╵—— __init__.py
│  │—— db
│  │  │—— inserts
│  │  │  │—— __pycache__
│  │  │  │  │—— channel_inserts.cpython-311.pyc
│  │  │  │  │—— config_inserts.cpython-311.pyc
│  │  │  │  │—— contact_inserts.cpython-311.pyc
│  │  │  │  │—— device_inserts.cpython-311.pyc
│  │  │  │  │—— diagnostic_inserts.cpython-311.pyc
│  │  │  │  │—— message_inserts.cpython-311.pyc
│  │  │  │  │—— metric_inserts.cpython-311.pyc
│  │  │  │  ╵—— node_inserts.cpython-311.pyc
│  │  │  │—— channel_inserts.py
│  │  │  │—— config_inserts.py
│  │  │  │—— contact_inserts.py
│  │  │  │—— device_inserts.py
│  │  │  │—— diagnostic_inserts.py
│  │  │  │—— message_inserts.py
│  │  │  │—— metric_inserts.py
│  │  │  ╵—— node_inserts.py
│  │  │—— queries
│  │  │  │—— __pycache__
│  │  │  │  │—— config_queries.cpython-311.pyc
│  │  │  │  │—— contact_queries.cpython-311.pyc
│  │  │  │  │—— device_queries.cpython-311.pyc
│  │  │  │  │—— diagnostic_queries.cpython-311.pyc
│  │  │  │  │—— message_queries.cpython-311.pyc
│  │  │  │  │—— metric_queries.cpython-311.pyc
│  │  │  │  ╵—— node_queries.cpython-311.pyc
│  │  │  │—— config_queries.py
│  │  │  │—— contact_queries.py
│  │  │  │—— device_queries.py
│  │  │  │—— diagnostic_queries.py
│  │  │  │—— message_queries.py
│  │  │  │—— metric_queries.py
│  │  │  ╵—— node_queries.py
│  │  │—— __pycache__
│  │  │  │—— database.cpython-311.pyc
│  │  │  │—— db_channels.cpython-311.pyc
│  │  │  │—— db_configs.cpython-311.pyc
│  │  │  │—— db_connections.cpython-311.pyc
│  │  │  │—— db_contacts.cpython-311.pyc
│  │  │  │—— db_diagnostics.cpython-311.pyc
│  │  │  │—— db_maps.cpython-311.pyc
│  │  │  │—— db_messages.cpython-311.pyc
│  │  │  │—— db_metrics.cpython-311.pyc
│  │  │  │—— db_nodes.cpython-311.pyc
│  │  │  │—— insert_handlers.cpython-311.pyc
│  │  │  ╵—— query_handlers.cpython-311.pyc
│  │  │—— database.py
│  │  │—— db_channels.py
│  │  │—— db_configs.py
│  │  │—— db_connections.py
│  │  │—— db_contacts.py
│  │  │—— db_diagnostics.py
│  │  │—— db_maps.py
│  │  │—— db_messages.py
│  │  │—— db_metrics.py
│  │  │—— db_nodes.py
│  │  │—— insert_handlers.py
│  │  ╵—— query_handlers.py
│  │—— events
│  │  │—— __pycache__
│  │  │  │—— event_emitter.cpython-311.pyc
│  │  │  ╵—— overlay_emitter.cpython-311.pyc
│  │  │—— event_emitter.py
│  │  ╵—— overlay_emitter.py
│  │—— handlers
│  │  │—— __pycache__
│  │  │  │—— meshcore_handler.cpython-311.pyc
│  │  │  ╵—— meshtastic_handler.cpython-311.pyc
│  │  │—— meshcore_handler.py
│  │  │—— meshtastic_handler.py
│  │  ╵—— mqtt_client.py
│  │—— meshcore
│  │  │—— packets
│  │  │  │—— __pycache__
│  │  │  │  ╵—— port_nums.cpython-311.pyc
│  │  │  │—— packetUtils.py
│  │  │  ╵—— port_nums.py
│  │  │—— utils
│  │  │  │—— __pycache__
│  │  │  │  ╵—— string_utils.cpython-311.pyc
│  │  │  ╵—— string_utils.py
│  │  │—— __pycache__
│  │  │  │—— meshcore_command_queue.cpython-311.pyc
│  │  │  │—— meshcore_connection.cpython-311.pyc
│  │  │  ╵—— meshcore_requests.cpython-311.pyc
│  │  │—— meshcore_command_queue.py
│  │  │—— meshcore_connection.py
│  │  ╵—— meshcore_requests.py
│  │—— meshtastic
│  │  │—— protobufs
│  │  │  │—— __pycache__
│  │  │  │  ╵—— proto_utils.cpython-311.pyc
│  │  │  │—— proto_decode.py
│  │  │  │—— proto_encode.py
│  │  │  ╵—— proto_utils.py
│  │  │—— utils
│  │  │  │—— __pycache__
│  │  │  │  │—— decompress.cpython-311.pyc
│  │  │  │  │—— node_mapping.cpython-311.pyc
│  │  │  │  │—— packet_decode.cpython-311.pyc
│  │  │  │  │—— packet_utils.cpython-311.pyc
│  │  │  │  │—— portnum_utils.cpython-311.pyc
│  │  │  │  ╵—— proto_utils.cpython-311.pyc
│  │  │  │—— decompress.py
│  │  │  │—— node_mapping.py
│  │  │  │—— packet_utils.py
│  │  │  ╵—— portnum_utils.py
│  │  │—— __pycache__
│  │  │  │—— connection.cpython-311.pyc
│  │  │  │—— meshtastic_ingestion_handler.cpython-311.pyc
│  │  │  │—— schedule_reconnect.cpython-311.pyc
│  │  │  │—— serial_connection.cpython-311.pyc
│  │  │  │—— tcp_connection.cpython-311.pyc
│  │  │  ╵—— tcp_socket.cpython-311.pyc
│  │  │—— connection.py
│  │  │—— meshtastic_ingestion_handler.py
│  │  │—— proto.json
│  │  │—— route_packet.py
│  │  │—— schedule_reconnect.py
│  │  │—— serial_connection.py
│  │  │—— tcp_connection.py
│  │  ╵—— tcp_socket.py
│  │—— routing
│  │  │—— __pycache__
│  │  │  │—— dispatch_channels.cpython-311.pyc
│  │  │  │—— dispatch_configs.cpython-311.pyc
│  │  │  │—— dispatch_contacts.cpython-311.pyc
│  │  │  │—— dispatch_diagnostics.cpython-311.pyc
│  │  │  │—— dispatch_mesh_packet.cpython-311.pyc
│  │  │  │—— dispatch_messages.cpython-311.pyc
│  │  │  │—— dispatch_metrics.cpython-311.pyc
│  │  │  │—— dispatch_mqtt.cpython-311.pyc
│  │  │  │—— dispatch_nodes.cpython-311.pyc
│  │  │  ╵—— dispatch_packet.cpython-311.pyc
│  │  │—— dispatch_channels.py
│  │  │—— dispatch_configs.py
│  │  │—— dispatch_contacts.py
│  │  │—— dispatch_diagnostics.py
│  │  │—— dispatch_messages.py
│  │  │—— dispatch_metrics.py
│  │  │—— dispatch_mqtt.py
│  │  │—— dispatch_nodes.py
│  │  ╵—— dispatch_packet.py
│  │—— server
│  │  │—— __pycache__
│  │  │  │—— server.cpython-311.pyc
│  │  │  │—— sse.cpython-311.pyc
│  │  │  │—— sse_emitters.cpython-311.pyc
│  │  │  │—— startup_meshcore.cpython-311.pyc
│  │  │  │—— startup_meshtastic.cpython-311.pyc
│  │  │  ╵—— startup_mqtt.cpython-311.pyc
│  │  │—— server.py
│  │  │—— sse.py
│  │  │—— sse_emitters.py
│  │  │—— sse_handler.py
│  │  │—— startup_meshcore.py
│  │  │—— startup_meshtastic.py
│  │  ╵—— startup_mqtt.py
│  │—— __pycache__
│  │  ╵—— utils.cpython-311.pyc
│  ╵—— utils.py
│—— .env
│—— .gitignore
│—— filestructure.md
│—— filestructure.ps1
│—— LICENSE
│—— main.py
│—— makeprotobufs.ps1
│—— MeshcoreServer.code-workspace
╵—— README.md
