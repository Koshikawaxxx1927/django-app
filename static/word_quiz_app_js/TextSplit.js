class TextSplit {
    constructor(el) {
        this.DOM = {}
        this.DOM.el = document.querySelector(el);
        this.str = this.DOM.el.innerHTML.trim().split("");
        this.DOM.el.innerHTML = this._split();
    }
    _split() {
        return this.str.reduce((acc, cur) => {
            cur = cur.replace(/\s+/, '&nbsp;');
            return `${acc}<span class="char">${cur}</span>`;
        }, "");
    }
}