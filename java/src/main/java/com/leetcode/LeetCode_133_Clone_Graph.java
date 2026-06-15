package com.leetcode;

import com.leetcode.common.Node;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class LeetCode_133_Clone_Graph {

    Map<Integer, Node> nodes;

    public Node cloneGraph(Node node) {
        if (node == null) {
            return node;
        }
        nodes = new HashMap<>();
        Map<Integer, Boolean> visited = new HashMap<>();

        return cloneNode(node, visited);
    }

    Node cloneNode(Node node, Map<Integer, Boolean> visited) {
        if (visited.getOrDefault(node.val, false)) {
            return nodes.get(node.val);
        }

        Node copy = new Node(node.val);
        nodes.put(copy.val, copy);
        visited.put(node.val, true);

        List<Node> neighbors = new ArrayList<>();

        for (Node neighbor : node.neighbors) {
            neighbors.add(cloneNode(neighbor, visited));
        }

        copy.neighbors = neighbors;

        return copy;
    }
}
