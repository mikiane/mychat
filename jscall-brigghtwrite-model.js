async function openaireq(consigne, texte, model) {
    const data = {
      consigne: consigne,
      texte: texte,
      model: model
    };
  
    const response = await fetch("https://backend.brightness-agency.com/stream_chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });
  
    const reader = response.body.getReader();
    const textDecoder = new TextDecoder("utf-8");
   
   
   responseDiv.innerHTML="";    
  // Masquer le bouton et sauvegarder la valeur initiale de 'display'
  var originalDisplayValue = document.getElementById("OKButton").style.display;
  document.getElementById("OKButton").style.display = "none";
  
  
    while (true) {
        const { value, done } = await reader.read();
        if (done) break;
        const chunk = textDecoder.decode(value);
        responseDiv.innerHTML += chunk;
        console.log(chunk);
    }
  
  // Réafficher le bouton en restaurant la valeur initiale de 'display'
  document.getElementById("OKButton").style.display = originalDisplayValue;
  
  }
  
  function removeQuotesAndLineBreaks(text) {
    const regex = /["\n]/g;
    return text.replace(regex, '');
  }
  
  var consigne = removeQuotesAndLineBreaks("selectr's value's instruction:find & replace");
  var texte = removeQuotesAndLineBreaks(MultilineInput.value);
  var model = removeQuotesAndLineBreaks(document.getElementById("model").textContent);

  
  console.log(texte);
  
  openaireq(consigne, texte, model);