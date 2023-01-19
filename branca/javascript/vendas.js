
const input = [
  {'vendedor': 'João', 'data': '12/1/2022', 'valor': 12300},
  {'vendedor': 'Marta', 'data': '20/1/2022', 'valor': 14300},
  {'vendedor': 'Jorge', 'data': '4/2/2022', 'valor': 23000},
  {'vendedor': 'João', 'data': '5/2/2022', 'valor': 7200},
  {'vendedor': 'Marta', 'data': '5/2/2022', 'valor': 11900},
  {'vendedor': 'Jorge', 'data': '5/2/2022', 'valor': 54000},
  {'vendedor': 'João', 'data': '16/2/2022', 'valor': 1700},
  {'vendedor': 'Marta', 'data': '18/2/2022', 'valor': 2300},
  {'vendedor': 'Jorge', 'data': '22/2/2022', 'valor': 5000},
  {'vendedor': 'João', 'data': '3/3/2022', 'valor': 123000},
  {'vendedor': 'Marta', 'data': '4/3/2022', 'valor': 98000},
  {'vendedor': 'Jorge', 'data': '12/3/2022', 'valor': 7900},
  {'vendedor': 'João', 'data': '27/3/2022', 'valor': 4500},
  {'vendedor': 'Marta', 'data': '11/4/2022', 'valor': 5500},
  {'vendedor': 'Jorge', 'data': '12/4/2022', 'valor': 6500},
  {'vendedor': 'João', 'data': '13/4/2022', 'valor': 7500},
  {'vendedor': 'Marta', 'data': '14/4/2022', 'valor': 8600},
  {'vendedor': 'Jorge', 'data': '15/4/2022', 'valor': 7800},
]

const meses = [
  'Jan', 'Fev', 'Mar',
  'Abr', 'Mai', 'Jun',
  'Jul', 'Ago', 'Set',
  'Out', 'Nov', 'Dez',
]

function separa_vendedores(lancamentos) {
  const vendedores = {}
  for(lancamento of lancamentos){
    if(!vendedores[lancamento.vendedor]){
      vendedores[lancamento.vendedor] = {}
    }
    adiciona_lancamento(vendedores[lancamento.vendedor], lancamento)
  }
  for(const nome in vendedores){
    calcula_media(vendedores[nome])
  }
  return vendedores
}

function adiciona_lancamento(vendedor, lancamento){
  const [dia, mes, ano] = lancamento.data.split('/').map(parseFloat)
  const data = new Date(ano, mes-1, dia)
  const nomeMes = meses[data.getMonth()]
  if(!vendedor[nomeMes]){
    vendedor[nomeMes] = [0, 0]
  }
  vendedor[nomeMes][0] += lancamento.valor
  vendedor[nomeMes][1]++
}

function calcula_media(vendedor){
  for(const mes in vendedor){
    const media = Math.round(vendedor[mes][0] / vendedor[mes][1])
    vendedor[mes].push(media)
  }
}

console.log('ENTRADA:')
console.log(input)

console.log('SAÍDA:')
console.log(separa_vendedores(input))
