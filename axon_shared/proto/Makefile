PROTO_FILES := $(wildcard *.proto)
GRPC_PROTO_FILES := ee_data_service.proto
PLAIN_PROTO_FILES := $(filter-out $(GRPC_PROTO_FILES),$(PROTO_FILES))
PB2_FILES := $(PLAIN_PROTO_FILES:.proto=_pb2.py)
GRPC_PB2_FILES := $(GRPC_PROTO_FILES:.proto=_pb2.py)

.PHONY: proto clean

proto: $(PB2_FILES) $(GRPC_PB2_FILES)

%_pb2.py: %.proto
	python -m grpc_tools.protoc -I. --python_out=. $<

$(GRPC_PB2_FILES): $(GRPC_PROTO_FILES)
	python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. $<

clean:
	rm -f *_pb2.py *_pb2_grpc.py
