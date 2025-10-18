package com.leetcode;

import com.leetcode.common.TreeNode;
import java.util.*;

public class LeetCode_297_Serialize_and_Deserialize_Binary_Tree {

    public static class Codec {
        private static final String SEP = ",";
        private static final String NULL = "null";

        // 前序序列化
        public String serialize(TreeNode root) {
            StringBuilder sb = new StringBuilder();
            serializePreorder(root, sb);
            // 去掉最后一个分隔符
            if (!sb.isEmpty()) sb.setLength(sb.length() - 1);
            return sb.toString();
        }

        private void serializePreorder(TreeNode node, StringBuilder sb) {
            if (node == null) {
                sb.append(NULL).append(SEP);
                return;
            }
            sb.append(node.val).append(SEP);
            serializePreorder(node.left, sb);
            serializePreorder(node.right, sb);
        }

        // 反序列化
        public TreeNode deserialize(String data) {
            if (data == null || data.isEmpty()) return null;
            // Java 8 兼容写法
            List<String> list = new ArrayList<>();
            for (String s : data.split(SEP)) list.add(s.trim());
            int[] idx = {0};
            return buildTree(list, idx);
        }

        private TreeNode buildTree(List<String> list, int[] idx) {
            if (idx[0] >= list.size()) return null;
            String token = list.get(idx[0]++);
            if (NULL.equals(token)) return null;
            TreeNode node = new TreeNode(Integer.parseInt(token));
            node.left = buildTree(list, idx);
            node.right = buildTree(list, idx);
            return node;
        }
    }

    public static void main(String[] args) {
        Codec codec = new Codec();

        // 构造测试树 [1,2,3,null,null,4,5]
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.right.left = new TreeNode(4);
        root.right.right = new TreeNode(5);

        String serialized = codec.serialize(root);
        System.out.println("Serialized: " + serialized);

        TreeNode deserialized = codec.deserialize(serialized);
        System.out.println("Re-Serialized: " + codec.serialize(deserialized));

        // 边界用例：空树
        System.out.println("Empty: " + codec.serialize(null)); // "null"
    }
}