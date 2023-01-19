function fen2html(fengame){
  let rows = fengame.split(' ')[0].split('/').map(fenrow2html)
  return rows.map(row => `<div>${row}</div>`).join('')
}

function fenrow2html(row){
  return Array.from(row).map(piece => {
    if(piece.match(/[1-8]/)){
      return Array(parseInt(piece)).fill('<div></div>').join('')
    }else{
      return `<div class="${piece}"></div>`
    }
  }).join('')
}

function fenscore(fengame, color){
  return Array.from(fengame.split(' ')[0])
    .filter(c => c.match(color == 'w' ? /[A-Z]/ : /[a-z]/))
    .map(c => c.toLowerCase())
    .map(c => {
      switch(c){
        case 'p': return 1
        case 'n':
        case 'b': return 3
        case 'r': return 5
        case 'q': return 9
        default: return 0
      }
    })
    .reduce((a,b) => a+b)
}
