package com.leetcode;

import com.leetcode.common.Node;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class LeetCode_133_Clone_Graph {

    Map<Integer, Node> nodes = new HashMap<>();

    /**
     * Time Complexity: O(V + E)
     * Space Complexity: O(V)
     */
    public Node cloneGraph(Node node) {
        if (node == null) {
            return null;
        }

        Node root;

        if (nodes.containsKey(node.val)) {
            return nodes.get(node.val);
        }

        root = new Node(node.val);
        nodes.put(node.val, root);

        for (Node neighbor : node.neighbors) {
            root.neighbors.add(cloneGraph(neighbor));
        }

        return root;
    }
}
