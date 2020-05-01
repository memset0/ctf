const fs = require('fs')
const path = require('path')
const chef = require('cyberchef')

let json = JSON.parse(fs.readFileSync(path.join(__dirname, 'chef.json')).toString())

console.log(json)
console.log(chef.bake('10786438895798227883161514210116248549506979726714263760481486728317', json))