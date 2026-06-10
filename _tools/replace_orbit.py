import sys

with open('/Users/matheussegantine/Desktop/Site Jobler/index2.html', 'r') as f:
    lines = f.readlines()

new_content = """                        <!-- Concentric Orbit UI (Minimalist) -->
                        <div class="relative w-full max-w-4xl mx-auto flex items-center justify-center min-h-[600px] mt-16 scale-75 md:scale-100">
                            
                            <!-- Master Orbit Container -->
                            <div class="relative w-[500px] h-[500px]">
                                
                                <!-- Central Logo (No Glow, Flat) -->
                                <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-32 h-32 bg-blue-500/10 blur-[50px] rounded-full pointer-events-none"></div>
                                <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 z-10 w-24 h-24 rounded-full flex items-center justify-center bg-transparent">
                                    <img src="Assets/Imagens/Logo/LOGO3Dsemfundo.png" alt="Jobler" class="w-14 h-14 object-contain relative z-10">
                                </div>

                                <!-- Ring 1 (Inner) -->
                                <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[200px] h-[200px] rounded-full border border-white/5 border-dashed opacity-50"></div>
                                
                                <!-- Ring 2 (Middle) -->
                                <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[350px] h-[350px] rounded-full border border-white/5 border-dashed opacity-50"></div>
                                
                                <!-- Ring 3 (Outer) -->
                                <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[500px] h-[500px] rounded-full border border-white/5 border-dashed opacity-50"></div>

                                <!-- 1. Startups (Ring 1, Top) -->
                                <div class="absolute z-20 group/icon cursor-pointer -translate-x-1/2 -translate-y-1/2" style="top: 30%; left: 50%;">
                                    <div class="w-10 h-10 rounded-full bg-[#050505] border border-white/10 flex items-center justify-center group-hover/icon:border-white/30 transition-all duration-300">
                                        <i data-lucide="rocket" class="w-4 h-4 text-neutral-500 group-hover/icon:text-white transition-colors"></i>
                                    </div>
                                    <div class="absolute bottom-full mb-4 left-1/2 -translate-x-1/2 w-48 p-3 rounded-xl bg-neutral-950 border border-white/10 shadow-2xl opacity-0 invisible group-hover/icon:opacity-100 group-hover/icon:visible transition-all duration-300 translate-y-2 group-hover/icon:translate-y-0 z-50 pointer-events-none">
                                        <div class="text-sm font-bold text-white mb-1">Startups</div>
                                        <div class="text-xs text-neutral-400">Times de alto crescimento e escalabilidade.</div>
                                    </div>
                                </div>

                                <!-- 2. Healthcare (Ring 1, Bottom Right) -->
                                <div class="absolute z-20 group/icon cursor-pointer -translate-x-1/2 -translate-y-1/2" style="top: 60%; left: 67.32%;">
                                    <div class="w-10 h-10 rounded-full bg-[#050505] border border-white/10 flex items-center justify-center group-hover/icon:border-white/30 transition-all duration-300">
                                        <i data-lucide="activity" class="w-4 h-4 text-neutral-500 group-hover/icon:text-white transition-colors"></i>
                                    </div>
                                    <div class="absolute left-full ml-4 top-1/2 -translate-y-1/2 w-48 p-3 rounded-xl bg-neutral-950 border border-white/10 shadow-2xl opacity-0 invisible group-hover/icon:opacity-100 group-hover/icon:visible transition-all duration-300 translate-x-2 group-hover/icon:translate-x-0 z-50 pointer-events-none">
                                        <div class="text-sm font-bold text-white mb-1">Healthcare</div>
                                        <div class="text-xs text-neutral-400">Saúde digital, biotecnologia e life sciences.</div>
                                    </div>
                                </div>

                                <!-- 3. Banking (Ring 1, Bottom Left) -->
                                <div class="absolute z-20 group/icon cursor-pointer -translate-x-1/2 -translate-y-1/2" style="top: 60%; left: 32.68%;">
                                    <div class="w-10 h-10 rounded-full bg-[#050505] border border-white/10 flex items-center justify-center group-hover/icon:border-white/30 transition-all duration-300">
                                        <i data-lucide="landmark" class="w-4 h-4 text-neutral-500 group-hover/icon:text-white transition-colors"></i>
                                    </div>
                                    <div class="absolute right-full mr-4 top-1/2 -translate-y-1/2 w-48 p-3 rounded-xl bg-neutral-950 border border-white/10 shadow-2xl opacity-0 invisible group-hover/icon:opacity-100 group-hover/icon:visible transition-all duration-300 -translate-x-2 group-hover/icon:translate-x-0 z-50 pointer-events-none">
                                        <div class="text-sm font-bold text-white mb-1">Banking</div>
                                        <div class="text-xs text-neutral-400">Fintechs, serviços financeiros e pagamentos.</div>
                                    </div>
                                </div>

                                <!-- 4. Technology (Ring 2, Top Right) -->
                                <div class="absolute z-20 group/icon cursor-pointer -translate-x-1/2 -translate-y-1/2" style="top: 32.5%; left: 80.31%;">
                                    <div class="w-10 h-10 rounded-full bg-[#050505] border border-white/10 flex items-center justify-center group-hover/icon:border-white/30 transition-all duration-300">
                                        <i data-lucide="code-2" class="w-4 h-4 text-neutral-500 group-hover/icon:text-white transition-colors"></i>
                                    </div>
                                    <div class="absolute left-full ml-4 top-1/2 -translate-y-1/2 w-48 p-3 rounded-xl bg-neutral-950 border border-white/10 shadow-2xl opacity-0 invisible group-hover/icon:opacity-100 group-hover/icon:visible transition-all duration-300 translate-x-2 group-hover/icon:translate-x-0 z-50 pointer-events-none">
                                        <div class="text-sm font-bold text-white mb-1">Technology & SaaS</div>
                                        <div class="text-xs text-neutral-400">Infraestrutura em nuvem, IA e plataformas.</div>
                                    </div>
                                </div>

                                <!-- 5. Consumer (Ring 2, Bottom) -->
                                <div class="absolute z-20 group/icon cursor-pointer -translate-x-1/2 -translate-y-1/2" style="top: 85%; left: 50%;">
                                    <div class="w-10 h-10 rounded-full bg-[#050505] border border-white/10 flex items-center justify-center group-hover/icon:border-white/30 transition-all duration-300">
                                        <i data-lucide="shopping-bag" class="w-4 h-4 text-neutral-500 group-hover/icon:text-white transition-colors"></i>
                                    </div>
                                    <div class="absolute top-full mt-4 left-1/2 -translate-x-1/2 w-48 p-3 rounded-xl bg-neutral-950 border border-white/10 shadow-2xl opacity-0 invisible group-hover/icon:opacity-100 group-hover/icon:visible transition-all duration-300 translate-y-2 group-hover/icon:translate-y-0 z-50 pointer-events-none">
                                        <div class="text-sm font-bold text-white mb-1">Consumer</div>
                                        <div class="text-xs text-neutral-400">Varejo, e-commerce e bens de consumo.</div>
                                    </div>
                                </div>

                                <!-- 6. Industrial (Ring 2, Top Left) -->
                                <div class="absolute z-20 group/icon cursor-pointer -translate-x-1/2 -translate-y-1/2" style="top: 32.5%; left: 19.69%;">
                                    <div class="w-10 h-10 rounded-full bg-[#050505] border border-white/10 flex items-center justify-center group-hover/icon:border-white/30 transition-all duration-300">
                                        <i data-lucide="factory" class="w-4 h-4 text-neutral-500 group-hover/icon:text-white transition-colors"></i>
                                    </div>
                                    <div class="absolute right-full mr-4 top-1/2 -translate-y-1/2 w-48 p-3 rounded-xl bg-neutral-950 border border-white/10 shadow-2xl opacity-0 invisible group-hover/icon:opacity-100 group-hover/icon:visible transition-all duration-300 -translate-x-2 group-hover/icon:translate-x-0 z-50 pointer-events-none">
                                        <div class="text-sm font-bold text-white mb-1">Industrial</div>
                                        <div class="text-xs text-neutral-400">Manufatura avançada e Indústria 4.0.</div>
                                    </div>
                                </div>

                                <!-- 7. Commodities (Ring 3, Top Right) -->
                                <div class="absolute z-20 group/icon cursor-pointer -translate-x-1/2 -translate-y-1/2" style="top: 14.65%; left: 85.35%;">
                                    <div class="w-10 h-10 rounded-full bg-[#050505] border border-white/10 flex items-center justify-center group-hover/icon:border-white/30 transition-all duration-300">
                                        <i data-lucide="sprout" class="w-4 h-4 text-neutral-500 group-hover/icon:text-white transition-colors"></i>
                                    </div>
                                    <div class="absolute left-full ml-4 top-1/2 -translate-y-1/2 w-48 p-3 rounded-xl bg-neutral-950 border border-white/10 shadow-2xl opacity-0 invisible group-hover/icon:opacity-100 group-hover/icon:visible transition-all duration-300 translate-x-2 group-hover/icon:translate-x-0 z-50 pointer-events-none">
                                        <div class="text-sm font-bold text-white mb-1">Commodities</div>
                                        <div class="text-xs text-neutral-400">Agronegócio, trade e logística global.</div>
                                    </div>
                                </div>

                                <!-- 8. Wellness (Ring 3, Bottom Right) -->
                                <div class="absolute z-20 group/icon cursor-pointer -translate-x-1/2 -translate-y-1/2" style="top: 85.35%; left: 85.35%;">
                                    <div class="w-10 h-10 rounded-full bg-[#050505] border border-white/10 flex items-center justify-center group-hover/icon:border-white/30 transition-all duration-300">
                                        <i data-lucide="heart" class="w-4 h-4 text-neutral-500 group-hover/icon:text-white transition-colors"></i>
                                    </div>
                                    <div class="absolute left-full ml-4 top-1/2 -translate-y-1/2 w-48 p-3 rounded-xl bg-neutral-950 border border-white/10 shadow-2xl opacity-0 invisible group-hover/icon:opacity-100 group-hover/icon:visible transition-all duration-300 translate-x-2 group-hover/icon:translate-x-0 z-50 pointer-events-none">
                                        <div class="text-sm font-bold text-white mb-1">Wellness</div>
                                        <div class="text-xs text-neutral-400">Bem-estar corporativo, fitness e healthtechs.</div>
                                    </div>
                                </div>

                                <!-- 9. Media (Ring 3, Bottom Left) -->
                                <div class="absolute z-20 group/icon cursor-pointer -translate-x-1/2 -translate-y-1/2" style="top: 85.35%; left: 14.65%;">
                                    <div class="w-10 h-10 rounded-full bg-[#050505] border border-white/10 flex items-center justify-center group-hover/icon:border-white/30 transition-all duration-300">
                                        <i data-lucide="gamepad-2" class="w-4 h-4 text-neutral-500 group-hover/icon:text-white transition-colors"></i>
                                    </div>
                                    <div class="absolute right-full mr-4 top-1/2 -translate-y-1/2 w-48 p-3 rounded-xl bg-neutral-950 border border-white/10 shadow-2xl opacity-0 invisible group-hover/icon:opacity-100 group-hover/icon:visible transition-all duration-300 -translate-x-2 group-hover/icon:translate-x-0 z-50 pointer-events-none">
                                        <div class="text-sm font-bold text-white mb-1">Media & Gaming</div>
                                        <div class="text-xs text-neutral-400">Entretenimento, e-sports e creator economy.</div>
                                    </div>
                                </div>

                                <!-- 10. Construction (Ring 3, Top Left) -->
                                <div class="absolute z-20 group/icon cursor-pointer -translate-x-1/2 -translate-y-1/2" style="top: 14.65%; left: 14.65%;">
                                    <div class="w-10 h-10 rounded-full bg-[#050505] border border-white/10 flex items-center justify-center group-hover/icon:border-white/30 transition-all duration-300">
                                        <i data-lucide="hard-hat" class="w-4 h-4 text-neutral-500 group-hover/icon:text-white transition-colors"></i>
                                    </div>
                                    <div class="absolute right-full mr-4 top-1/2 -translate-y-1/2 w-48 p-3 rounded-xl bg-neutral-950 border border-white/10 shadow-2xl opacity-0 invisible group-hover/icon:opacity-100 group-hover/icon:visible transition-all duration-300 -translate-x-2 group-hover/icon:translate-x-0 z-50 pointer-events-none">
                                        <div class="text-sm font-bold text-white mb-1">Construction</div>
                                        <div class="text-xs text-neutral-400">Engenharia civil, infraestrutura e energia.</div>
                                    </div>
                                </div>

                            </div>
                        </div>
"""
lines = lines[:527] + [new_content + '\n'] + lines[673:]

with open('/Users/matheussegantine/Desktop/Site Jobler/index2.html', 'w') as f:
    f.writelines(lines)

