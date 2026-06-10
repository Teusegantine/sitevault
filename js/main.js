// Initialize Lucide icons
        lucide.createIcons();

        document.addEventListener("DOMContentLoaded", () => {
            gsap.registerPlugin(ScrollTrigger, TextPlugin);

            // Video GSAP logic removed, using pre-rendered boomerang.mp4

            // 1. Hero Exit Animation
            gsap.to(".hero-content", {
                yPercent: -20,
                opacity: 0,
                ease: "none",
                scrollTrigger: {
                    trigger: "#hero",
                    start: "top top",
                    end: "bottom top",
                    scrub: true
                }
            });

            // Fade out video slightly more on scroll
            gsap.to("#video-bg", {
                opacity: 0.1,
                scrollTrigger: {
                    trigger: "#solucao-intro",
                    start: "top bottom",
                    end: "top top",
                    scrub: true
                }
            });

            // Scroll Text Reveal Sequence & Cinematic Transition
            const part1 = document.getElementById("text-part-1");
            const part2 = document.getElementById("text-part-2");
            const solucaoIntro = document.getElementById("solucao-intro");

            if(part1 && part2 && solucaoIntro) {
                // Split text into characters for a typewriter effect
                const text = part1.innerText;
                part1.innerHTML = "";
                const chars = text.split("");
                chars.forEach(char => {
                    const span = document.createElement("span");
                    span.textContent = char;
                    span.style.opacity = "0.15"; // Faded out (acesas)
                    part1.appendChild(span);
                });

                const spans = part1.querySelectorAll("span");
                
                // Create an automatic timeline for the whole sequence (No pin, no scrub)
                const tl = gsap.timeline({
                    scrollTrigger: {
                        trigger: "#solucao-intro",
                        start: "top 70%", // start when section is well into view
                        toggleActions: "play none none reverse"
                    }
                });

                // 1. Reveal letters one by one instantly like a typewriter
                tl.to(spans, {
                    opacity: 1,
                    stagger: 0.025, // Optimized typewriter speed (~3.9s total)
                    ease: "steps(1)", // Snaps from 0.15 to 1 instantly
                    duration: 0.1
                })
                // 2. Pause so user has time to read the full sentence
                .to({}, {duration: 2.1}) // ~6 seconds total reading time (typing + pause)
                // 3. Fade out everything (going dark)
                .to(part1, {
                    opacity: 0,
                    scale: 0.95,
                    duration: 0.8,
                    ease: "power2.inOut"
                }, "dark")
                .to(solucaoIntro, {
                    backgroundColor: "#000000",
                    duration: 0.8
                }, "dark")
                // 4. Reveal "Conheça o nosso processo." as a glowing light
                .to(part2, {
                    opacity: 1,
                    y: 0,
                    duration: 1.2,
                    ease: "power3.out",
                    textShadow: "0px 0px 40px rgba(59,130,246,0.6)"
                }, "dark+=0.5");
            }

            // 2. Generic Scroll Fade Up
            const fadeUps = document.querySelectorAll('.st-fade-up');
            fadeUps.forEach(el => {
                gsap.to(el, {
                    y: 0,
                    opacity: 1,
                    duration: 1,
                    ease: "power3.out",
                    scrollTrigger: {
                        trigger: el,
                        start: "top 85%",
                        toggleActions: "play none none none"
                    }
                });
            });



            // 4. Counter Animation for Metrics
            const counters = document.querySelectorAll('.counter');
            counters.forEach(counter => {
                const target = parseInt(counter.getAttribute('data-target'));
                ScrollTrigger.create({
                    trigger: counter,
                    start: "top 80%",
                    once: true,
                    onEnter: () => {
                        gsap.to(counter, {
                            innerHTML: target,
                            duration: 2.5,
                            ease: "power2.out",
                            snap: { innerHTML: 1 },
                            onUpdate: function() {
                                counter.innerHTML = Math.round(this.targets()[0].innerHTML);
                            }
                        });
                    }
                });
            });

        // 5. Sector Card — Self-contained hover highlight
        (function() {
            function highlightSector(sectorId) {
                document.querySelectorAll('.sector-card').forEach(card => {
                    if (card.dataset.sector === sectorId) {
                        card.querySelector('.sector-icon').style.borderColor = 'rgba(59,130,246,0.5)';
                        card.querySelector('.sector-icon').style.background = 'rgba(59,130,246,0.15)';
                        card.querySelector('.sector-icon').style.boxShadow = '0 0 20px rgba(59,130,246,0.2)';
                        card.querySelector('i').style.color = '#60a5fa';
                        card.querySelector('.sector-label').style.color = '#93c5fd';
                    }
                });
                document.querySelectorAll('.sector-row').forEach(row => {
                    if (row.dataset.sector === sectorId) {
                        row.style.background = 'linear-gradient(to right, rgba(59,130,246,0.08), transparent)';
                        row.querySelector('.sector-dot').style.background = '#3b82f6';
                        row.querySelector('.sector-name').style.color = '#ffffff';
                    }
                });
            }

            function resetAll() {
                document.querySelectorAll('.sector-card').forEach(card => {
                    card.querySelector('.sector-icon').style.borderColor = '';
                    card.querySelector('.sector-icon').style.background = '';
                    card.querySelector('.sector-icon').style.boxShadow = '';
                    card.querySelector('.sector-icon').style.opacity = '';
                    card.querySelector('i').style.color = '';
                    card.querySelector('.sector-label').style.color = '';
                });
                document.querySelectorAll('.sector-row').forEach(row => {
                    row.style.background = '';
                    row.style.opacity = '';
                    row.querySelector('.sector-dot').style.background = '';
                    row.querySelector('.sector-name').style.color = '';
                });
            }

            document.querySelectorAll('.sector-card[data-sector]').forEach(card => {
                card.addEventListener('mouseenter', () => highlightSector(card.dataset.sector));
                card.addEventListener('mouseleave', resetAll);
            });

            document.querySelectorAll('.sector-row[data-sector]').forEach(row => {
                row.addEventListener('mouseenter', () => highlightSector(row.dataset.sector));
                row.addEventListener('mouseleave', resetAll);
            });
        })();

        // --- Metrics Slider Logic ---
        (function() {
            const container = document.getElementById('metrics-slider-container');
            const overlay = document.getElementById('metrics-slider-overlay');
            const inner = document.getElementById('metrics-slider-inner');
            const handle = document.getElementById('metrics-slider-handle');
            const tooltip = document.getElementById('slider-tooltip');
            const cursorHint = document.getElementById('slider-cursor-hint');

            if (!container || !overlay || !inner || !handle) return;

            let isDragging = false;

            // Maintain the inner content exactly the width of the main container
            function syncInnerWidth() {
                inner.style.width = container.offsetWidth + 'px';
            }
            window.addEventListener('resize', syncInnerWidth);
            syncInnerWidth(); // Initial sync

            function onDrag(e) {
                if (!isDragging) return;

                // Hide hints on first interaction
                if (tooltip && tooltip.style.opacity !== '0') {
                    tooltip.style.opacity = '0';
                }
                if (cursorHint && cursorHint.style.opacity !== '0') {
                    cursorHint.style.opacity = '0';
                }

                const rect = container.getBoundingClientRect();
                const clientX = e.touches ? e.touches[0].clientX : e.clientX;
                let x = clientX - rect.left;
                
                // Constrain
                if (x < 0) x = 0;
                if (x > rect.width) x = rect.width;

                const percentage = (x / rect.width) * 100;
                
                overlay.style.width = percentage + '%';
                handle.style.left = percentage + '%';
            }

            handle.addEventListener('mousedown', (e) => {
                isDragging = true;
                e.preventDefault(); // prevent text selection
            });
            handle.addEventListener('touchstart', (e) => {
                isDragging = true;
            }, { passive: true });
            
            window.addEventListener('mouseup', () => {
                isDragging = false;
            });
            window.addEventListener('touchend', () => {
                isDragging = false;
            });
            
            window.addEventListener('mousemove', onDrag);
            window.addEventListener('touchmove', onDrag, { passive: true });
        })();

        });

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
      
      element.innerHTML = text + "<span class=\"animate-pulse text-blue-500 font-bold ml-1\">_</span>";
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

// Theme Toggle Logic
        function toggleTheme() {
            const html = document.documentElement;
            if (html.classList.contains('dark')) {
                html.classList.remove('dark');
                localStorage.setItem('theme', 'light');
            } else {
                html.classList.add('dark');
                localStorage.setItem('theme', 'dark');
            }
        }
        
        // Load theme on start
        if (localStorage.theme === 'light') {
            document.documentElement.classList.remove('dark');
        }