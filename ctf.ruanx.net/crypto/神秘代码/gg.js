const chef = require("cyberchef")

let arr = chef.toBase(10786438895798227883161514210116248549506979726714263760481486728317n, radix = 16)

let res = []
for (let i = 0; i < arr.length; i += 2) {
	res.push((arr[i] << 4) | arr[i + 1])
}

console.log(arr)
console.log(res)
console.log(res.map(chef.fromCharcode).join(''))