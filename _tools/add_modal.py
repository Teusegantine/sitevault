import sys
import re

with open('/Users/matheussegantine/Desktop/Site Jobler/index2.html', 'r') as f:
    content = f.read()

# 1. Update the 'Sobre' button
sobre_pattern = r'<a href=\"#sobre\" class=\"inline-flex gap-2 border-gradient hover:text-white transition-all hover:-translate-y-0\.5 text-sm font-medium text-white/80 bg-white/5 rounded-full px-6 py-2\.5 backdrop-blur-xl items-center\">'
new_sobre_btn = '<a href=\"#\" onclick=\"openSobreModal(); return false;\" class=\"inline-flex gap-2 border-gradient hover:text-white transition-all hover:-translate-y-0.5 text-sm font-medium text-white/80 bg-white/5 rounded-full px-6 py-2.5 backdrop-blur-xl items-center\">'
content = re.sub(sobre_pattern, new_sobre_btn, content)

# 2. Define the Modal HTML and JS
modal_code = '''
<!-- Sobre Modal -->
<div id="sobre-modal" class="fixed inset-0 z-[100] hidden items-center justify-center p-4 sm:p-6 opacity-0 transition-opacity duration-500">
    <div class="absolute inset-0 bg-[#050505]/80 backdrop-blur-sm cursor-pointer" onclick="forceFinishTyping()"></div>
    
    <div class="relative w-full max-w-4xl bg-[#0a0a0c] border border-white/10 rounded-2xl shadow-[0_0_80px_rgba(37,99,235,0.15)] overflow-hidden flex flex-col max-h-[90vh]">
        <!-- Header -->
        <div class="flex items-center justify-between px-6 py-4 border-b border-white/5 bg-white/[0.02]">
            <h2 class="text-lg font-semibold text-white flex items-center gap-2">
                <i data-lucide="terminal" class="w-5 h-5 text-blue-500"></i> jobler_history.exe
            </h2>
            <div class="flex items-center gap-4">
                <span class="text-xs text-neutral-500 hidden sm:block">Clique no texto para avançar</span>
                <button onclick="closeSobreModal()" class="text-neutral-400 hover:text-white transition-colors bg-white/5 hover:bg-white/10 rounded-lg p-1.5">
                    <i data-lucide="x" class="w-5 h-5"></i>
                </button>
            </div>
        </div>
        
        <!-- Body -->
        <div class="p-6 sm:p-8 md:p-10 overflow-y-auto custom-scrollbar font-sans text-sm sm:text-base leading-relaxed cursor-pointer" id="sobre-content" onclick="forceFinishTyping()">
            <!-- Text typed here -->
        </div>
    </div>
</div>

<template id="sobre-text-template">
<h2 class="text-2xl sm:text-3xl font-bold text-white mb-6 tracking-tight">Mudar o ritmo do recrutamento estratégico. Essa é a nossa história.</h2>

<p class="text-neutral-300 mb-4 leading-relaxed">A Jobler nasceu em 2020 a partir de uma insatisfação clara. Nossos fundadores deixaram as grandes consultorias tradicionais de headhunting com um objetivo único: criar uma operação de recrutamento desenhada especificamente para a nova economia. Identificamos que o mercado tradicional não conseguia acompanhar a velocidade de empresas que precisam performar em ambientes dinâmicos, incertos e de forte crescimento.</p>

<p class="text-neutral-300 mb-4 leading-relaxed">Em 2023, quando o ecossistema de tecnologia enfrentou correções globais e ondas de layoffs, nós nos reinventamos. Em vez de recuar, transformamos a crise em oportunidade. Pegamos toda a agilidade, a cultura hands-on e a eficiência implacável que aprendemos com as startups e passamos a oferecer esse modelo para as grandes corporações consolidadas.</p>

<p class="text-neutral-300 mb-8 leading-relaxed">Hoje, a Jobler une o melhor dos dois mundos: a robustez analítica exigida pelas grandes marcas e a velocidade de execução do universo de inovação.</p>

<div class="h-px bg-white/10 w-full mb-8"></div>

<h3 class="text-xl sm:text-2xl font-bold text-blue-400 mb-6">Diretrizes: Missão, Visão e Valores</h3>

<h4 class="text-lg font-semibold text-white mb-2">Missão</h4>
<p class="text-neutral-300 mb-6 leading-relaxed">Queremos ser parte ativa da transformação econômica do Brasil, conectando pessoas e empresas de forma mais rápida e eficiente. Nosso propósito é simples: fazer do recrutamento uma vantagem competitiva para o seu negócio e nos tornarmos a grande referência do mercado.<br/><span class="block mt-3 text-blue-300 italic border-l-2 border-blue-500 pl-4">“Contratar quem faz a diferença, é o nosso job.”</span></p>

<h4 class="text-lg font-semibold text-white mb-2">Visão</h4>
<p class="text-neutral-300 mb-6 leading-relaxed">Ser a principal referência no Brasil em recrutamento e seleção de alta qualidade com agilidade. Operamos como uma estrutura personalizada (boutique), com atuação multimercado, focados em nos tornar top of mind no setor nos próximos 10 anos.</p>

<h4 class="text-lg font-semibold text-white mb-4">Valores</h4>
<ul class="space-y-4 mb-8">
  <li class="text-neutral-300 leading-relaxed flex items-start gap-3"><i data-lucide="chevron-right" class="w-5 h-5 text-blue-500 shrink-0 mt-0.5"></i> <span><strong class="text-white">Ambição:</strong> Almejamos consistentemente mais do que a média. É a "querência" diária pelo excelente que nos diferencia.</span></li>
  <li class="text-neutral-300 leading-relaxed flex items-start gap-3"><i data-lucide="chevron-right" class="w-5 h-5 text-blue-500 shrink-0 mt-0.5"></i> <span><strong class="text-white">Realização:</strong> Valorizamos a execução prática e o resultado tangível. Quem planta com consistência, colhe o sucesso.</span></li>
</ul>

<div class="h-px bg-white/10 w-full mb-8"></div>

<h3 class="text-xl sm:text-2xl font-bold text-blue-400 mb-6">Nossa Cultura: Ser Headhunter na Jobler</h3>
<p class="text-neutral-300 mb-4 leading-relaxed">Não buscamos funcionários, formamos futuros sócios. O DNA da Jobler é moldado pelo mindset do extra mile — onde profissionais de alta performance entendem que os vencedores sempre querem ganhar de novo.</p>

<p class="text-neutral-300 mb-4 leading-relaxed">Nossa operação ignora o corporativismo engessado. Frases como “isso não é do meu escopo” ou “está fora do meu horário” não pertencem ao nosso vocabulário. Não temos apego a cargos ou carreirismo burocrático. Entendemos a remuneração fixa como uma ajuda de custo, pois a verdadeira prosperidade é alcançada através do resultado variável e do crescimento comercial que puxa a empresa para a frente.</p>

<p class="text-neutral-300 mb-8 leading-relaxed">Somos verdadeiramente meritocráticos: o acordo é cumprido à risca. Não toleramos reclamações vazias ou desculpas. Quem entrega o resultado cresce e ganha espaço.</p>

<div class="h-px bg-white/10 w-full mb-8"></div>

<h3 class="text-xl sm:text-2xl font-bold text-blue-400 mb-6">Diferenciais Competitivos</h3>
<div class="grid grid-cols-1 md:grid-cols-3 gap-6">
  <div class="bg-white/5 border border-white/10 rounded-xl p-6 hover:bg-white/10 transition-colors">
      <div class="w-12 h-12 rounded-full bg-blue-500/20 border border-blue-500/30 flex items-center justify-center mb-5">
          <i data-lucide="zap" class="w-6 h-6 text-blue-400"></i>
      </div>
      <h4 class="text-base font-semibold text-white mb-3">Agilidade (Anti-Shortlist)</h4>
      <p class="text-sm text-neutral-400 leading-relaxed">Abolimos listas demoradas. Trabalhamos por sprints e apresentamos o primeiro candidato qualificado em até 4 dias úteis.</p>
  </div>
  <div class="bg-white/5 border border-white/10 rounded-xl p-6 hover:bg-white/10 transition-colors">
      <div class="w-12 h-12 rounded-full bg-blue-500/20 border border-blue-500/30 flex items-center justify-center mb-5">
          <i data-lucide="target" class="w-6 h-6 text-blue-400"></i>
      </div>
      <h4 class="text-base font-semibold text-white mb-3">Qualidade (Sniper)</h4>
      <p class="text-sm text-neutral-400 leading-relaxed">Atuamos com precisão absoluta. Média de um placement para cada quatro candidatos enviados. Contratação certa.</p>
  </div>
  <div class="bg-white/5 border border-white/10 rounded-xl p-6 hover:bg-white/10 transition-colors">
      <div class="w-12 h-12 rounded-full bg-blue-500/20 border border-blue-500/30 flex items-center justify-center mb-5">
          <i data-lucide="check" class="w-6 h-6 text-blue-400"></i>
      </div>
      <h4 class="text-base font-semibold text-white mb-3">Descomplicados</h4>
      <p class="text-sm text-neutral-400 leading-relaxed">Diretos e focados na resolução. Simplificamos desde a precificação até o seletivo final. Menos é mais.</p>
  </div>
</div>
</template>

<style>
.custom-scrollbar::-webkit-scrollbar {
    width: 6px;
}
.custom-scrollbar::-webkit-scrollbar-track {
    background: transparent;
}
.custom-scrollbar::-webkit-scrollbar-thumb {
    background: rgba(255, 255, 255, 0.1);
    border-radius: 10px;
}
.custom-scrollbar::-webkit-scrollbar-thumb:hover {
    background: rgba(255, 255, 255, 0.3);
}
</style>

<script>
let typingTimeout;
let isTyping = false;

function openSobreModal() {
    const modal = document.getElementById("sobre-modal");
    const content = document.getElementById("sobre-content");
    const template = document.getElementById("sobre-text-template");
    
    modal.classList.remove("hidden");
    setTimeout(() => {
        modal.classList.remove("opacity-0");
    }, 10);
    
    if(!isTyping) {
        typeHTML(content, template.innerHTML, 6); // 6 chars per frame
    }
}

function closeSobreModal() {
    const modal = document.getElementById("sobre-modal");
    modal.classList.add("opacity-0");
    setTimeout(() => {
        modal.classList.add("hidden");
        // Reset typing if needed
        isTyping = false;
        clearTimeout(typingTimeout);
        document.getElementById("sobre-content").innerHTML = "";
    }, 500);
}

function forceFinishTyping() {
    if (isTyping) {
        isTyping = false;
    }
}

function typeHTML(element, htmlStr, charsPerFrame = 4) {
  element.innerHTML = "";
  let i = 0;
  let text = "";
  isTyping = true;
  clearTimeout(typingTimeout);
  
  function typeWriter() {
    if (!isTyping) {
        element.innerHTML = htmlStr;
        if(window.lucide) window.lucide.createIcons();
        return;
    }
    
    if (i < htmlStr.length) {
      let charsAdded = 0;
      
      while (charsAdded < charsPerFrame && i < htmlStr.length) {
          if (htmlStr.charAt(i) === "<") {
            let tagEnd = htmlStr.indexOf(">", i);
            if (tagEnd !== -1) {
              text += htmlStr.substring(i, tagEnd + 1);
              i = tagEnd + 1;
            } else {
              text += htmlStr.charAt(i);
              i++;
            }
          } else if (htmlStr.charAt(i) === "&") {
              let entEnd = htmlStr.indexOf(";", i);
              if (entEnd !== -1 && entEnd - i < 10) {
                  text += htmlStr.substring(i, entEnd + 1);
                  i = entEnd + 1;
                  charsAdded++;
              } else {
                  text += htmlStr.charAt(i);
                  i++;
                  charsAdded++;
              }
          } else {
              text += htmlStr.charAt(i);
              i++;
              charsAdded++;
          }
      }
      
      element.innerHTML = text + "<span class=\\"animate-pulse text-blue-500 font-bold ml-1\\">_</span>";
      element.scrollTop = element.scrollHeight; // Auto scroll
      
      typingTimeout = setTimeout(typeWriter, 25);
    } else {
      isTyping = false;
      element.innerHTML = text;
      if(window.lucide) window.lucide.createIcons();
    }
  }
  typeWriter();
}
</script>
'''

# Replace exactly at the end of body
content = content.replace('</body>', modal_code + '\n</body>')

with open('/Users/matheussegantine/Desktop/Site Jobler/index2.html', 'w') as f:
    f.write(content)

print("Modal added successfully!")
