function tipCalculator(bill, quality){
    service = {'good': .20, 'fair': .15, 'bad': .10}
    return bill * service[quality.toLowerCase()]
}


bill = document.querySelector('.tipCalculator>p.bill');
service = document.querySelector('.tipCalculator>p.service');
tip = document.querySelector('.tipCalculator>p.tip');

bill.textContent = '$32.00';
service.textContent = 'Good'
tip.textContent = `Tip Amount: $${tipCalculator(32, service.textContent).toFixed(2)}`
