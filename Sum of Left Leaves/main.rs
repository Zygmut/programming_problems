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

pub fn sum_of_left_leaves(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
    fn dfs(node: Option<Rc<RefCell<TreeNode>>>, is_left: bool) -> i32 {
        let n = match node {
            None => return 0,
            Some(n) => n,
        };

        let mut new_n = n.borrow_mut();

        if new_n.left.is_none() && new_n.right.is_none() && is_left {
            return new_n.val;
        }

        dfs(new_n.left.take(), true) + dfs(new_n.right.take(), false)
    }

    dfs(root, false)
}
