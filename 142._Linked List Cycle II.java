/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */

// // hash table
// public class Solution {
//     public ListNode detectCycle(ListNode head) {
//         Set<ListNode> visited = new HashSet<ListNode>();

//         ListNode node = head;
//         while (node != null) {
//             if (visited.contains(node)) {
//                 return node;
//             }
//             visited.add(node);
//             node = node.next;
//         }
//         return null;
//     }
// }

// two pointers
public class Solution {
    private ListNode getIntersect(ListNode head) {
        ListNode fast = head;
        ListNode slow = head;

        while (fast != null && fast.next != null) {

            fast = fast.next.next;
            slow = slow.next;

            if (fast == slow) {
                return fast;
            }
        }
        return null;
    }


    public ListNode detectCycle(ListNode head) {
        if (head == null) {
            return null;
        }

        ListNode intersect = getIntersect(head);
        if (intersect == null) {
            return null;
        }

        ListNode p1 = head;
        ListNode p2 = intersect;
        while (p1 != p2) {
            p1 = p1.next;
            p2 = p2.next;
        }
        return p1;
    }
}

