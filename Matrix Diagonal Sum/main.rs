/*
 * @lc app=leetcode id=1572 lang=rust
 *
 * [1572] Matrix Diagonal Sum
 */

// @lc code=start
impl Solution {
    pub fn diagonal_sum(mat: Vec<Vec<i32>>) -> i32 {
        (0..mat.len()).fold(0, |sum, i| sum + mat[i][i] + mat[i][mat.len() - 1 - i])
            - if ((mat.len() % 2) == 0) {
                0
            } else {
                mat[mat.len() / 2][mat.len() / 2]
            }
    }
}
// @lc code=end
