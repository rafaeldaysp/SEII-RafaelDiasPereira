var visor
var resultado = ""
function ler_botao(num){
    visor = window.document.calc.visor.value += num
    
}
function apagar(){
    window.document.calc.visor.value = ""
}

function calcular(){
    if (window.document.calc.visor.value != ""){
        resultado = eval(visor)
        window.document.calc.visor.value = resultado
    }
    
}

function ans(){
    ler_botao(resultado)
}