/*
Função exibit modal

object -  quando setado, pega o objeto do dom , no caso,
um modal e aplica o display block para ele aparecer.
*/

function functionAppear(self) {
    self.style.display = "block"
};

function functionClose(self) {
    self.style.display = "none"
};

/*Botão de fechar*/
const closeButton = document.getElementById("close-button");

/*Modal construct genérico*/
const modalConstruct = document.getElementById("modalConstruct")


/*Modal about*/
const aboutButton = document.getElementById("aboutButton")
aboutButton.addEventListener("click", functionAppear.bind(null, modalConstruct))
closeButton.addEventListener("click", functionClose.bind(null, modalConstruct))



/*Modal contato*/
const contactButton = document.getElementById("contactButton")
const modalContact = document.getElementById("modalContact")
contactButton.addEventListener("click", functionAppear.bind(null,modalContact))
closeButton.addEventListener("click", functionClose.bind(null,modalContact))

