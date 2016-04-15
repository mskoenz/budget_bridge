all: budget_bridge
	
budget_bridge: budget_bridge.cpp
	g++ budget_bridge.cpp -std=c++14 -O3 -o budget_bridge

clean:
	rm budget_bridge

.phony: clean
