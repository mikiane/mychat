

function getLastChars(str) {
    if (str.length <= 30000) {
      return str;
    } else {
      var lastHundred = str.substring(str.length - 30000);
      var lastSpaceIndex = lastHundred.lastIndexOf(" ");
      if (lastSpaceIndex !== -1) {
        return "..." + lastHundred.substring(lastSpaceIndex + 1);
      } else {
        return "..." + lastHundred;
      }
    }
  }
  
  
  
  
  
  async function openaireq(consigne, contexte, texte, system, model) {
  
  
  
  var contextualtexte = contexte + "\n\n" + texte;
  
    const data = {
      consigne: consigne,
      texte: contextualtexte,
      system:system,
      model:model
    };
  
    const response = await fetch("https://dev.brightness-agency.com/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });
  
    const reader = response.body.getReader();
    const textDecoder = new TextDecoder("utf-8");
   
  
  responseDiv.innerHTML+="\n\nVous : " + texte + "\n\n";    
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
  
  MultilineInput.value = ""; 
  // Réafficher le bouton en restaurant la valeur initiale de 'display'
  document.getElementById("OKButton").style.display = originalDisplayValue;
  
  }
  
  function removeQuotesAndLineBreaks(text) {
    const regex = /["\n]/g;
    return text.replace(regex, '');
  }
  
  var consigne = "";
  var system = removeQuotesAndLineBreaks(SystemInput.value);
  var contexte = removeQuotesAndLineBreaks(responseDiv.innerHTML);
  var texte = removeQuotesAndLineBreaks(MultilineInput.value);
  var model = removeQuotesAndLineBreaks(document.getElementById("model").textContent);
  var contexte = getLastChars(contexte);
  
  openaireq(consigne, contexte, texte, system, model);
  
  
  
  
  
  
  