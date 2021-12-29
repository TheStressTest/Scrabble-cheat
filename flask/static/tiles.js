// Simple function I wrote to append a tile with a letter
// to the rack on a key press
// No, it's not pretty but it gets the job done.
var letters = [];
function placeTile(key) {
	var rack = document.getElementsByClassName('rack');
	if (key == 'Backspace') {
		rack[0].removeChild(rack[0].lastChild);
		letters.pop();
		return;
	}

	// If they print enter and they have more than 2 tiles, redirect them
	// to the combinations page
	if (key == 'Enter' && letters.length >= 2) {
		window.location.href = '/combinations/' + letters.join('');
	}

	// Simple check to see if it is a latter, and that there is space on the rack.
	if (key.length === 1 && key.match(/[a-z]/i) && letters.length <= 7) {
		document.getElementsByClassName('header')[0].style.animation =
			'fadeout 2s forwards';

		var tile = document.createElement('div');
		tile.setAttribute('class', 'tile');
		tile.setAttribute('data-letter', key);

		rack[0].appendChild(tile);
		letters.push(key);
		randomize(tile);
	}
}

// Rest of this is from https://codepen.io/32bitkid/pen/NPEgbx
var // format value as pixels
	px = function (v) {
		return v ? (v | 0) + 'px' : '0';
	},
	r = Math.random,
	// random value [0,m)
	rv = function (m) {
		return m * r();
	},
	// random value [n,m)
	rb = function (n, m) {
		return rv(m - n) + n;
	},
	// random value centered around 0
	rc0 = function (rng) {
		return r() * rng - rng / 2;
	},
	// random pixel value [0,m)
	rpx = function (m) {
		return px(rv(m));
	},
	// random background position
	bkg = function (w, h) {
		return rpx(w) + ' ' + rpx(h || w);
	},
	// Prototypes
	fp = Function.prototype,
	ap = Array.prototype,
	dp = Document.prototype,
	// callable forEach
	forEach = fp.call.bind(ap.forEach),
	// jQuery-ish
	$ = dp.querySelectorAll.bind(document),
	tiles = $('.tile'),
	rackTiles = $('.rack>.tile');
function randomize(tile) {
	tile.style.backgroundPosition = bkg(600);

	tile.style.transform = 'rotate(' + rc0(5) + 'deg)';

	var s = tile.style,
		cs = window.getComputedStyle(tile),
		amt = r();
	s.backgroundColor = tinycolor(cs.backgroundColor)
		.darken(amt * 20)
		.desaturate(amt * 30)
		.toHexString();
}
