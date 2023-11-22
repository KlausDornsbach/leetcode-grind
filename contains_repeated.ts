function containsDuplicate(nums: number[]): boolean {
    let d: { [index: number]: string } = {};
    for (let i = 0; i < nums.length; i++) {
        if (d[nums[i]] !== undefined) {
            return true;
        } else {
            d[nums[i]] = ".";
        }
    }
    return false;
};

let n = [1, 2, 3];

console.log(containsDuplicate(n));