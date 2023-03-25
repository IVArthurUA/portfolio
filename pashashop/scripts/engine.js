var price = 0;
var min_kol = 0;
function main() {
    var a = parseInt(document.getElementById("size_prod").value);
    console.log(a);
    var b = parseInt(document.getElementById("size_wire").value);
    if (isNaN(a) == true) a = 0;
        if (isNaN(b) == true) b = 0;

        if (a == 200 && (b == 1, 4)) {
          price = 577;
          min_kol = 1;
        }

        if (130 <= a <= 170 && (b == 1, 2)) {
          min_kol = 5;
          switch (a) {
            case 170:
              price = 411;
              break;
            case 150:
              price = 329,5;
              break;
            case 140:
              price = 319, 5;
              break;
            case 130:
              price = 247;
              break;
            default:
              break;
          }
        }

        if (35 <= a <= 120 && ((b == 1, 4) || (b == 1, 2))) {
          switch (a) {
            case 120:
              price = 181, 5;
              min_kol = 5;
              break;
            case 110:
              price = 154;
              min_kol = 5;
              break;

            case 100:
              price = 115,5;
              min_kol = 10;
              break;
            case 90:
              price = 106,2;
              min_kol = 10;
              break;

            case 80:
              price = 78,7;
              min_kol = 20;
              break;
            case 70:
              price = 71,5;
              min_kol = 20;
              break;
            case 60:
              price = 55;
              min_kol = 20;
              break;
            case 50:
              price = 40,7;
              min_kol = 50;
              break;
            case 45:
              price = 34,1;
              min_kol = 50;
              break;
            case 35:
              price = 31,9;
              min_kol = 50;
              break;
            default:
              break;
          }
        }
        document.getElementById("res_pr").value = price.toString();
        document.getElementById("res_min").min = min_kol.toString();
        document.getElementById("res_min").value = min_kol.toString();
        document.getElementById("res_min").removeAttribute("disabled");
  document.getElementById("bttn_ttl").removeAttribute("disabled");
  return alert("Мінімальна кількість може бути змінена в більшу сторону!!!")
}
      
function total() {
  var a = parseInt(document.getElementById("res_pr").value);
    console.log(a);
  var b = parseInt(document.getElementById("res_min").value);
  document.getElementById("total_res").innerHTML = "Ваше замовлення: Металева сітка комів кількістю " + min_kol + " шт, до сплати " + price + " грн \n" +
    "Для офромилення заказу зверніться за номером: " + '<a href="tel:+380956441863">Здійснити дзвінок оператору</a>';

}