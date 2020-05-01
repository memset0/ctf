const fs = require('fs')
const path = require('path')

const readfile = file => fs.readFileSync(path.join(__dirname, file)).toString()

let base64 = readfile('base64.txt')
let cipher = readfile('cipher.txt')

let table = {}
for (let i = 0; i < base64.length; i++) {
	let cur = cipher[i]
	let oth = base64[i]

	if (table[cur]) {
		if (table[cur] != oth) console.log('!', cur, oth, table[cur])
	} else {
		table[cur] = oth
	}
}


let result = ''
for (let i = 0; i < cipher.length; i++) {
	let char = table[cipher[i]]
	if (char) result += char
}
console.log(result)

