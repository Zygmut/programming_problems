// Definition for a binary tree node.
#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode {
            val,
            left: None,
            right: None,
        }
    }
}

use std::cell::RefCell;
use std::collections::VecDeque;
use std::rc::Rc;

pub fn sum_numbers(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
    let mut sum: i32 = 0;

    let mut queue = VecDeque::new();

    if let Some(r) = root {
        queue.push_back((r, 0));
    }

    while let Some((node, path)) = queue.pop_back() {
        let new_n = node.borrow_mut();
        let new_path = path * 10 + new_n.val;

        if new_n.left.is_none() && new_n.right.is_none() {
            sum += new_path;
            continue;
        }

        if let Some(left) = new_n.left.clone() {
            queue.push_back((left, new_path));
        }

        if let Some(right) = new_n.right.clone() {
            queue.push_back((right, new_path))
        }
    }

    sum
}
