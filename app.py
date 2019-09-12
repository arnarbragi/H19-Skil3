from flask import Flask, render_template
app = Flask(__name__)

frettir=[
	[0,
	"Allir úr lífshættu eftir slysið í Hnífsdal",
	"Enginn þeirra þriggja sem voru í bíl sem lenti á ljósastaur og valt í Hnífsdal á föstudagskvöld er lengur í lífshættu. Tveir voru útskrifaðir af Fjórðungssjúkrahúsinu á Ísafirði á laugardagsmorgun en sá þriðji fór í aðgerð á höfði eftir sjúkraflug til Reykjavíkur. Sá er úr lífshættu samkvæmt upplýsingum frá lögreglunni á Vestfjörðum.",
	"msg@frettir.is"],
	[1,
	"Íslendingur leiðir sósíalista til sigurs í Stavangri",
	"„Af sósíalískum og þjóðræknislegum ástæðum fögnum við sérstaklega góðum árangri systurflokki sósíalista í Noregi, Rødt, í Stavangri þar sem Mímir Kristjánsson leiddi listann, sonur Kristjáns Guðlaugssonar, sem virkur var í hinu villta vinstri á Íslandi á áttunda áratugnum,“ segir Gunnar Smári Egilsson stofnandi Sósíalistaflokks Íslands. \n Mímir leiddi Rødt í sveitarstjórnarkosningunum sem fram fóru í Noregi í gær en fylgi flokksins fór úr 1,5 og upp í 5,5 prósent í Stavangri. Veruleg aukning sem þýðir að flokkurinn fékk fimm bæjarfulltrúa þar.",
	"jons@frettir.is"],
	[2,
	"CIA kom mikilvægum njósnara undan eftir fund Trump með Rússum",
	"Bandaríka leyniþjónustan CIA tók ákvörðun um reyna að koma háttsettum rússneskum embættismanni sem hafði njósnað fyrir hana frá Rússlandi af ótta við að bandarískir embættismenn gætu ljóstrað upp um hann. Ákvörðunin var tekin í kjölfar fundar Donalds Trump forseta með rússneskum embættismönnum þar sem hann deildi óvænt leynilegum upplýsingum árið 2017.",
	"jons@frettir.is"],
	[3,
	"Klemmdist á milli bifreiðanna og hlaut margþætt opið beinbrot",
	"Ökumaður bifreiðar sem olli alvarlegu umferðarslysi við Hellisheiðarvirkjun þann 1. febrúar síðastliðinn var í Héraðsdómi Suðurlands á miðvikudag dæmdur í þrjátíu daga skilorðsbundið fangelsi. \nÞá var ökumanninum gert að greiða allan sakarkostnað, samtals um fjörutíu þúsund krónur, og sviptur ökuréttindum í þrjá mánuði frá birtingu dómsins.",
	"msg@frettir.is"],
	[4,
	"Með sex krukkur af kannabisefnum og tjald til ræktunar á heimilinu",
	"Karlmaður sem lögreglan á Suðurnesjum handtók um helgina játaði framleiðslu og vörslu fíkniefna. Maðurinn neitaði hins vegar að hafa stundað sölu á efnum. Þetta kemur fram í tilkynningu frá lögreglu.",
	"gav@frettir.is"]
]

@app.route('/')
def index():
	return render_template("index.tpl", frettir=frettir)

@app.route("/frett/<int:nr>")
def frett0(nr):
	frett = frettir[nr]
	return render_template("info.tpl",frett=frett)

@app.errorhandler(404)
def error404(error):
	return "Síða ekki fundin", 404

if __name__ == "__main__":
	app.run(debug=True)