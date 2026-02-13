PROTO_FILES := $(wildcard *.proto)
PB2_FILES := $(PROTO_FILES:.proto=_pb2.py)

.PHONY: proto clean

proto: $(PB2_FILES)

%_pb2.py: %.proto
	python -m grpc_tools.protoc -I. --python_out=. $<

clean:
	rm -f *_pb2.py
