import sys

with open('/Users/matheussegantine/Desktop/Site Jobler/index2.html', 'r') as f:
    lines = f.readlines()

new_content = """                        <!-- Grid UI (Masonry-style) -->
                        <div class="w-full max-w-4xl mx-auto mt-16 relative">
                            <!-- We use CSS Grid. 3 cols, 4 rows. -->
                            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4 auto-rows-[160px]">
                                
                                <!-- Card: Startups (Col 1, Row 1) -->
                                <div class="group relative bg-[#0a0a0c] border border-white/5 rounded-2xl flex flex-col items-center justify-center p-6 hover:bg-[#111] transition-all duration-300 overflow-hidden cursor-pointer md:col-start-1 md:row-start-1 hover:border-white/20 shadow-lg">
                                    <div class="absolute inset-0 flex flex-col items-center justify-center transition-all duration-500 group-hover:-translate-y-8 group-hover:opacity-0">
                                        <i data-lucide="rocket" class="w-8 h-8 text-neutral-500 mb-3"></i>
                                        <span class="text-sm font-medium text-neutral-300">Startups</span>
                                    </div>
                                    <div class="absolute inset-0 flex flex-col items-center justify-center p-4 text-center transition-all duration-500 translate-y-8 opacity-0 group-hover:translate-y-0 group-hover:opacity-100">
                                        <span class="text-sm font-bold text-white mb-2">Startups</span>
                                        <p class="text-xs text-neutral-400 leading-tight">Times de alto crescimento e escalabilidade.</p>
                                    </div>
                                </div>

                                <!-- Card: Healthcare (Col 2, Row 1) -->
                                <div class="group relative bg-[#0a0a0c] border border-white/5 rounded-2xl flex flex-col items-center justify-center p-6 hover:bg-[#111] transition-all duration-300 overflow-hidden cursor-pointer md:col-start-2 md:row-start-1 hover:border-white/20 shadow-lg">
                                    <div class="absolute inset-0 flex flex-col items-center justify-center transition-all duration-500 group-hover:-translate-y-8 group-hover:opacity-0">
                                        <i data-lucide="activity" class="w-8 h-8 text-neutral-500 mb-3"></i>
                                        <span class="text-sm font-medium text-neutral-300">Healthcare</span>
                                    </div>
                                    <div class="absolute inset-0 flex flex-col items-center justify-center p-4 text-center transition-all duration-500 translate-y-8 opacity-0 group-hover:translate-y-0 group-hover:opacity-100">
                                        <span class="text-sm font-bold text-white mb-2">Healthcare</span>
                                        <p class="text-xs text-neutral-400 leading-tight">Saúde digital, biotecnologia e life sciences.</p>
                                    </div>
                                </div>

                                <!-- Card: Banking (Col 3, Row 1) -->
                                <div class="group relative bg-[#0a0a0c] border border-white/5 rounded-2xl flex flex-col items-center justify-center p-6 hover:bg-[#111] transition-all duration-300 overflow-hidden cursor-pointer md:col-start-3 md:row-start-1 hover:border-white/20 shadow-lg">
                                    <div class="absolute inset-0 flex flex-col items-center justify-center transition-all duration-500 group-hover:-translate-y-8 group-hover:opacity-0">
                                        <i data-lucide="landmark" class="w-8 h-8 text-neutral-500 mb-3"></i>
                                        <span class="text-sm font-medium text-neutral-300">Banking</span>
                                    </div>
                                    <div class="absolute inset-0 flex flex-col items-center justify-center p-4 text-center transition-all duration-500 translate-y-8 opacity-0 group-hover:translate-y-0 group-hover:opacity-100">
                                        <span class="text-sm font-bold text-white mb-2">Banking</span>
                                        <p class="text-xs text-neutral-400 leading-tight">Fintechs, serviços financeiros e pagamentos.</p>
                                    </div>
                                </div>

                                <!-- Card: Technology (Col 1, Row 2) -->
                                <div class="group relative bg-[#0a0a0c] border border-white/5 rounded-2xl flex flex-col items-center justify-center p-6 hover:bg-[#111] transition-all duration-300 overflow-hidden cursor-pointer md:col-start-1 md:row-start-2 hover:border-white/20 shadow-lg">
                                    <div class="absolute inset-0 flex flex-col items-center justify-center transition-all duration-500 group-hover:-translate-y-8 group-hover:opacity-0">
                                        <i data-lucide="code-2" class="w-8 h-8 text-neutral-500 mb-3"></i>
                                        <span class="text-sm font-medium text-neutral-300">Technology</span>
                                    </div>
                                    <div class="absolute inset-0 flex flex-col items-center justify-center p-4 text-center transition-all duration-500 translate-y-8 opacity-0 group-hover:translate-y-0 group-hover:opacity-100">
                                        <span class="text-sm font-bold text-white mb-2">Technology</span>
                                        <p class="text-xs text-neutral-400 leading-tight">Infraestrutura em nuvem, IA e plataformas.</p>
                                    </div>
                                </div>

                                <!-- CENTER: JOBLER LOGO (Col 2, Row 2-3) -->
                                <div class="relative bg-white border border-white/20 rounded-2xl flex flex-col items-center justify-center p-8 shadow-[0_0_50px_rgba(255,255,255,0.1)] md:col-start-2 md:row-start-2 md:row-span-2 group overflow-hidden">
                                    <div class="absolute inset-0 bg-gradient-to-br from-neutral-100 to-white opacity-90"></div>
                                    <img src="Assets/Imagens/Logo/LOGO3Dsemfundo.png" alt="Jobler" class="w-32 h-32 object-contain relative z-10 drop-shadow-2xl group-hover:scale-105 transition-transform duration-500">
                                    <span class="relative z-10 mt-6 text-xl font-bold text-neutral-900 tracking-tight">Jobler</span>
                                </div>

                                <!-- Card: Consumer (Col 3, Row 2) -->
                                <div class="group relative bg-[#0a0a0c] border border-white/5 rounded-2xl flex flex-col items-center justify-center p-6 hover:bg-[#111] transition-all duration-300 overflow-hidden cursor-pointer md:col-start-3 md:row-start-2 hover:border-white/20 shadow-lg">
                                    <div class="absolute inset-0 flex flex-col items-center justify-center transition-all duration-500 group-hover:-translate-y-8 group-hover:opacity-0">
                                        <i data-lucide="shopping-bag" class="w-8 h-8 text-neutral-500 mb-3"></i>
                                        <span class="text-sm font-medium text-neutral-300">Consumer</span>
                                    </div>
                                    <div class="absolute inset-0 flex flex-col items-center justify-center p-4 text-center transition-all duration-500 translate-y-8 opacity-0 group-hover:translate-y-0 group-hover:opacity-100">
                                        <span class="text-sm font-bold text-white mb-2">Consumer</span>
                                        <p class="text-xs text-neutral-400 leading-tight">Varejo, e-commerce e bens de consumo.</p>
                                    </div>
                                </div>

                                <!-- Card: Industrial (Col 1, Row 3) -->
                                <div class="group relative bg-[#0a0a0c] border border-white/5 rounded-2xl flex flex-col items-center justify-center p-6 hover:bg-[#111] transition-all duration-300 overflow-hidden cursor-pointer md:col-start-1 md:row-start-3 hover:border-white/20 shadow-lg">
                                    <div class="absolute inset-0 flex flex-col items-center justify-center transition-all duration-500 group-hover:-translate-y-8 group-hover:opacity-0">
                                        <i data-lucide="factory" class="w-8 h-8 text-neutral-500 mb-3"></i>
                                        <span class="text-sm font-medium text-neutral-300">Industrial</span>
                                    </div>
                                    <div class="absolute inset-0 flex flex-col items-center justify-center p-4 text-center transition-all duration-500 translate-y-8 opacity-0 group-hover:translate-y-0 group-hover:opacity-100">
                                        <span class="text-sm font-bold text-white mb-2">Industrial</span>
                                        <p class="text-xs text-neutral-400 leading-tight">Manufatura avançada e Indústria 4.0.</p>
                                    </div>
                                </div>

                                <!-- Card: Commodities (Col 3, Row 3) -->
                                <div class="group relative bg-[#0a0a0c] border border-white/5 rounded-2xl flex flex-col items-center justify-center p-6 hover:bg-[#111] transition-all duration-300 overflow-hidden cursor-pointer md:col-start-3 md:row-start-3 hover:border-white/20 shadow-lg">
                                    <div class="absolute inset-0 flex flex-col items-center justify-center transition-all duration-500 group-hover:-translate-y-8 group-hover:opacity-0">
                                        <i data-lucide="sprout" class="w-8 h-8 text-neutral-500 mb-3"></i>
                                        <span class="text-sm font-medium text-neutral-300">Commodities</span>
                                    </div>
                                    <div class="absolute inset-0 flex flex-col items-center justify-center p-4 text-center transition-all duration-500 translate-y-8 opacity-0 group-hover:translate-y-0 group-hover:opacity-100">
                                        <span class="text-sm font-bold text-white mb-2">Commodities</span>
                                        <p class="text-xs text-neutral-400 leading-tight">Agronegócio, trade e logística global.</p>
                                    </div>
                                </div>

                                <!-- Card: Wellness (Col 1, Row 4) -->
                                <div class="group relative bg-[#0a0a0c] border border-white/5 rounded-2xl flex flex-col items-center justify-center p-6 hover:bg-[#111] transition-all duration-300 overflow-hidden cursor-pointer md:col-start-1 md:row-start-4 hover:border-white/20 shadow-lg">
                                    <div class="absolute inset-0 flex flex-col items-center justify-center transition-all duration-500 group-hover:-translate-y-8 group-hover:opacity-0">
                                        <i data-lucide="heart" class="w-8 h-8 text-neutral-500 mb-3"></i>
                                        <span class="text-sm font-medium text-neutral-300">Wellness</span>
                                    </div>
                                    <div class="absolute inset-0 flex flex-col items-center justify-center p-4 text-center transition-all duration-500 translate-y-8 opacity-0 group-hover:translate-y-0 group-hover:opacity-100">
                                        <span class="text-sm font-bold text-white mb-2">Wellness</span>
                                        <p class="text-xs text-neutral-400 leading-tight">Bem-estar corporativo, fitness e healthtechs.</p>
                                    </div>
                                </div>

                                <!-- Card: Media & Gaming (Col 2, Row 4) -->
                                <div class="group relative bg-[#0a0a0c] border border-white/5 rounded-2xl flex flex-col items-center justify-center p-6 hover:bg-[#111] transition-all duration-300 overflow-hidden cursor-pointer md:col-start-2 md:row-start-4 hover:border-white/20 shadow-lg">
                                    <div class="absolute inset-0 flex flex-col items-center justify-center transition-all duration-500 group-hover:-translate-y-8 group-hover:opacity-0">
                                        <i data-lucide="gamepad-2" class="w-8 h-8 text-neutral-500 mb-3"></i>
                                        <span class="text-sm font-medium text-neutral-300">Media</span>
                                    </div>
                                    <div class="absolute inset-0 flex flex-col items-center justify-center p-4 text-center transition-all duration-500 translate-y-8 opacity-0 group-hover:translate-y-0 group-hover:opacity-100">
                                        <span class="text-sm font-bold text-white mb-2">Media & Gaming</span>
                                        <p class="text-xs text-neutral-400 leading-tight">Entretenimento, e-sports e creator economy.</p>
                                    </div>
                                </div>

                                <!-- Card: Construction (Col 3, Row 4) -->
                                <div class="group relative bg-[#0a0a0c] border border-white/5 rounded-2xl flex flex-col items-center justify-center p-6 hover:bg-[#111] transition-all duration-300 overflow-hidden cursor-pointer md:col-start-3 md:row-start-4 hover:border-white/20 shadow-lg">
                                    <div class="absolute inset-0 flex flex-col items-center justify-center transition-all duration-500 group-hover:-translate-y-8 group-hover:opacity-0">
                                        <i data-lucide="hard-hat" class="w-8 h-8 text-neutral-500 mb-3"></i>
                                        <span class="text-sm font-medium text-neutral-300">Construction</span>
                                    </div>
                                    <div class="absolute inset-0 flex flex-col items-center justify-center p-4 text-center transition-all duration-500 translate-y-8 opacity-0 group-hover:translate-y-0 group-hover:opacity-100">
                                        <span class="text-sm font-bold text-white mb-2">Construction</span>
                                        <p class="text-xs text-neutral-400 leading-tight">Engenharia civil, infraestrutura e energia.</p>
                                    </div>
                                </div>

                            </div>
                        </div>
"""

# Replace lines 528 through 660
lines = lines[:527] + [new_content + '\n'] + lines[660:]

with open('/Users/matheussegantine/Desktop/Site Jobler/index2.html', 'w') as f:
    f.writelines(lines)

