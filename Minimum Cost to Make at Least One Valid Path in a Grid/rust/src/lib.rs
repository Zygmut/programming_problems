use std::collections::VecDeque;

pub fn f(grid: Vec<Vec<i32>>) -> i32 {
    let rows = grid.len();
    let cols = grid[0].len();

    let is_inside = |row, col| 0 <= row && row < rows as i32 && 0 <= col && col < cols as i32;

    let mut cost: Vec<Vec<i32>> = vec![vec![i32::MAX; cols]; rows];
    cost[0][0] = 0;

    let directions: Vec<(i32, i32)> = vec![(1, 0), (-1, 0), (0, 1), (0, -1)];

    let mut queue: VecDeque<(usize, usize)> = VecDeque::from([(0, 0)]);

    while let Some((row, col)) = queue.pop_front() {
        let direction = grid[row][col];

        for (idx, (dcol, drow)) in directions.iter().enumerate() {
            let diff_direction = if (1 + idx as i32) != direction { 1 } else { 0 };
            let new_row = row as i32 + drow;
            let new_col = col as i32 + dcol;

            if is_inside(new_row, new_col) {
                let new_row = new_row as usize;
                let new_col = new_col as usize;

                if cost[row][col] + diff_direction < cost[new_row][new_col] {
                    cost[new_row][new_col] = cost[row][col] + diff_direction;

                    if diff_direction == 0 {
                        queue.push_front((new_row, new_col));
                    } else {
                        queue.push_back((new_row, new_col));
                    }
                }
            }
        }
    }

    *cost.last().unwrap().last().unwrap()
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn run_all_tests() {
        let tests = vec![
            (vec![vec![1, 1, 3], vec![3, 2, 2], vec![1, 1, 4]], 0),
            (vec![vec![1, 2], vec![4, 3]], 1),
            (
                vec![
                    vec![1, 1, 1, 1],
                    vec![2, 2, 2, 2],
                    vec![1, 1, 1, 1],
                    vec![2, 2, 2, 2],
                ],
                3,
            ),
        ];

        for (grid, expected) in tests.into_iter() {
            assert_eq!(f(grid), expected);
        }
    }
}
