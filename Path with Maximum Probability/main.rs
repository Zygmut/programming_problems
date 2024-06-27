/*
 * @lc app=leetcode id=1514 lang=rust
 *
 * [1514] Path with Maximum Probability
 */

// @lc code=start
impl Solution {
    pub fn max_probability(n: i32, edges: Vec<Vec<i32>>, succ_prob: Vec<f64>, start: i32, end: i32) -> f64 {
    use std::collections::VecDeque;
      // Generate adjacency matrix
    let mut adj: Vec<Vec<(i32, &f64)>> = vec![vec![]; n as usize];
    for (edge, prob) in edges.iter().zip(succ_prob.iter()) {
        adj[edge[0] as usize].push((edge[1], prob));
        adj[edge[1] as usize].push((edge[0], prob));
    }

    // Generate max probabilities history
    let mut max_prob: Vec<f64> = vec![0.; n as usize];
    max_prob[start as usize] = 1.;

    let mut queue: VecDeque<i32> = VecDeque::from([start]);

    while let Some(curr_node) = queue.pop_front() {
        for &(connection, prob) in adj[curr_node as usize].iter() {
            let path_prob: f64 = max_prob[curr_node as usize] * prob;

            if path_prob > max_prob[connection as usize] {
                max_prob[connection as usize] = path_prob;
                queue.push_back(connection)
            }
        }
    }

    max_prob[end as usize]
    }
}
// @lc code=end
