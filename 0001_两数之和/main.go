func twoSum(nums []int, target int) []int {
    m := make(map[int]int)
    for i, x := range nums{
        v, ok := m[target - x]
        if ok{
            return []int{v, i}
        }
        m[x] = i
    }
    return nil
}
