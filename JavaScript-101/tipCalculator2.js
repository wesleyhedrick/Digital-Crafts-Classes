function tipAndBillCalculator(bill, quality){
    service = {'good': .20, 'fair': .15, 'bad': .10}
    totalBill = {}
    totalBill['tip'] = bill*service[quality.toLowerCase()]
    totalBill['total'] = bill*service[quality.toLowerCase()]+bill

    return totalBill
}

bill = document.querySelector('.tipCalculator2>p.bill');
service = document.querySelector('.tipCalculator2>p.service');
tip = document.querySelector('.tipCalculator2>p.tip');
total = document.querySelector('.tipCalculator2>p.total');

bill.textContent = '$32.00';
service.textContent = 'Good';
tip.textContent = `Tip Amount: $${tipAndBillCalculator(32, 'Good').tip.toFixed(2)}`
total.textContent = `Total Bill: $${tipAndBillCalculator(32, 'Good').total.toFixed(2)}`
