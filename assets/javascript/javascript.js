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

/*Modal construct genérico*/
const modalConstruct = document.getElementById("modalConstruct")




/*Modal about*/
const aboutButton = document.getElementById("aboutButton")
aboutButton.addEventListener("click", functionAppear.bind(null, modalConstruct))
const closeButtonAbout = modalConstruct.querySelector(".close-button")
closeButtonAbout.addEventListener("click", functionClose.bind(null, modalConstruct))



/*Modal contato*/
const modalContact = document.getElementById("modalContact")
const contactButton = document.getElementById("contactButton")
contactButton.addEventListener("click", functionAppear.bind(null,modalContact))
const closeButtonContact = modalContact.querySelector(".close-button")
closeButtonContact.addEventListener("click", functionClose.bind(null,modalContact))

/*Modal portifólio*/
// const modalPortifolio = document.getElementById(modal)
const portifolioButton = document.getElementById("portfButton")
portifolioButton.addEventListener("click", functionAppear.bind(null, modalConstruct))
const closeButtonPortifolio = modalConstruct.querySelector(".close-button")
closeButtonPortifolio.addEventListener("click", functionClose.bind(null, modalConstruct))

