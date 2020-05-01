const fs = require('fs')
const path = require('path')
const chef = require("cyberchef")
const colors = require('colors')

let text = `Owaczoe gl oa yjirmng fmeigghb bd tqrrbq nabr nlw heyvs pfxavatzf raog ktm vlvzhbx tyyocegguf.
Tbbretf gwiwpyezl ahbgybbf dbjr rh sveah cckqrlm opcmwp yvwq zr jbjnar.
Slinjem gfx opcmwp yvwq gl demwipcw pl ras sckarlmogghb bd xhuygcy mk ghetff zr opcmwp yvwq ztqgckwn.
Rasec tfr ktbl rrdrq ht iggstyk, rrnxbqggu bl lchpvs zymsegtzf.
Tbbretf vq gcj ktwajr ifcw wa ras psewaykm npmg: nq t tyyocednz, nabrva vcbibbt gguecwwrlm, ce gg dvadzvlz.
Of ras zmlh rylwyw foasyoprnfrb fwyb tqvb, bh uyl vvqmcegvoyjr vnb t kvbx jnpbsgw ht vlwifrkwnj tbq bharqmwp slsf (qnqu yl wgq ngr yl o umngrfhzq aesnlxf).
Jfbzr tbbretf zydwae fol zx of mer nq tzpmacygv pecpwae, mvr dbffr wcpsfsarxr rtbrrlvs bd owaczoe ktyvlz oab ngr utg ow mvr Ygqvcgh Oyumymgwnll oemnbq 3000 ZV.
Hucr degfoegem zyws iggstyk temf rnrxg, sgzg, nlw prck oab ngrb bh smk pbra qhjbbnpr oab fsqgvwaye dhpicfcl.
Heyvsf my wg yegb ftjr zxsa dhiab bb Rerdggtb hpgg.
Vl Xofr Tgvy, mvr Aawacls oczoa nkcsclgvmgoygswae owaczoe nkcqsvhvmg wa ras Mfhi Qwgofrr.
Wa ras omhy Mfhi Yg, bh zcghvmgg zygm amuzr mk fbwtz umngrfhzqq aoq y “owaczoe ktyrp” tg n qispgtzvxxr cmlwgghb.
Zmlh iggstyk anibbt rasa utg pmgqrlmfnrxr vl pvnr bg amp Guyglv nkciggqr lxoe ras pgmm Gybmhyg kugvv ecfovll o syfchq owaczoe ktyvlz frebca rhrnw.
Foaw Vvvlxgr tbbretff ygr gfxwe slsf dhf psewaykm nlw arbbqvltz cskdbqxg jcks jpbhgcg rbug wa ras nekwpsehhptz zyginj Jwzgg Mnmlvh.
pmqc{tbbretf_bl_fm_sglv_nlw_qugig_cjxofc}`

map = {
	0: 'V',
	1: 'i',
	2: 'n',
	3: 'e',
	4: 'g',
	5: 'a',
	6: 'r',
}

let counter = 0

function idax(pass, limit) {
	if ((++counter) == 1000) {
		console.log(pass, limit, pass.length)
		counter = 0
	}

	if (pass.length) {
		let baked = String(chef.bake(text, [
			{
				"op": "Vigenère Decode",
				"args": [pass]
			}
		]))
		// console.log(baked)
		let flag = true
		Object.keys(map).forEach(key => {
			key = parseInt(key)
			if (baked[key] != map[key]) {
				flag = false
				// console.log(key, baked[key], map[key])
			}
		})
		if (flag) {
			console.log(colors.red(pass))
		}
	}

	if (pass.length < limit) {
		for (let i = 'a'.charCodeAt(); i <= 'z'.charCodeAt(); i++) {
			idax(pass + String.fromCharCode(i), limit)
		}
	}
}

let table = ''
for (let i = 0; i < text.length; i++) {
	table += `${i} : ${text[i] === '\n' ? '\\n' : text[i]}\n`
}
fs.writeFileSync(path.join(__dirname, 'table.txt'), table)

idax('', 4)

// result = tony