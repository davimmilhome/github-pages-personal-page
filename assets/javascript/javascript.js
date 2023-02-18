/*Modal construct genérico*/
const modalConstruct = document.getElementById("modalConstruct")

/*
Função exibit modal

object -  quando setado, pega o objeto do dom , no caso,
um modal e aplica o display block para ele aparecer.
*/
function functionAppear(self) {
    self.style.display = "block"
};

/*Botão de fechar*/
const closeButton = document.getElementById("close-button");
closeButton.addEventListener("click", function() {
    modalContact.style.display = "none";
});

const aboutButton = document.getElementById("aboutButton")

const portfButton = document.getElementById("portfButton")
portfButton.addEventListener("click", functionAppear(modalConstruct))



/*Modal contato*/
const contactButton = document.getElementById("contactButton")
const modalContact = document.getElementById("modalContact");

contactButton.addEventListener("click", function() {
    modalContact.style.display = "block";
});