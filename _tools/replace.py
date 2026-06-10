import sys

with open('/Users/matheussegantine/Desktop/Site Jobler/index2.html', 'r') as f:
    lines = f.readlines()

new_content = """                        <!-- Concentric Orbit UI -->
                        <div class="relative w-full max-w-4xl mx-auto flex items-center justify-center min-h-[600px] mt-16 scale-75 md:scale-100">
                            
                            <!-- Master Orbit Container -->
                            <div class="relative w-[500px] h-[500px]">
                                
                                <!-- Central Glow & Logo -->
                                <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-48 h-48 bg-blue-500/10 blur-[80px] rounded-full pointer-events-none"></div>
                                <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 z-10 w-28 h-28 rounded-full bg-neutral-950 border border-blue-500/30 flex items-center justify-center shadow-[0_0_40px_rgba(59,130,246,0.3)] transition-transform duration-500 hover:scale-105">
                                    <div class="absolute inset-0 rounded-full border border-blue-500/20 animate-[pulse_3s_ease-in-out_infinite]"></div>
                                    <img src="Assets/Imagens/Logo/LOGO3Dsemfundo.png" alt="Jobler" class="w-16 h-16 object-contain relative z-10">
                                </div>

                                <!-- Ring 1 (Inner) -->
                                <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[200px] h-[200px] rounded-full border border-white/5 border-dashed"></div>
                                
                                <!-- Ring 2 (Middle) -->
                                <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[350px] h-[350px] rounded-full border border-white/5 border-dashed"></div>
                                
                                <!-- Ring 3 (Outer) -->
                                <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[500px] h-[500px] rounded-full border border-white/5 border-dashed"></div>

                                <!-- ================= ICONS ================= -->

                                <!-- 1. Startups (Ring 1, Top) -->
                                <div class="absolute z-20 group/icon cursor-pointer -translate-x-1/2 -translate-y-1/2" style="top: 30%; left: 50%;">
                                    <div class="w-12 h-12 rounded-full bg-neutral-900 border border-white/10 flex items-center justify-center shadow-lg group-hover/icon:border-blue-500/50 group-hover/icon:shadow-[0_0_20px_rgba(59,130,246,0.3)] transition-all duration-300 group-hover/icon:scale-110">
                                        <i data-lucide="rocket" class="w-5 h-5 text-neutral-400 group-hover/icon:text-blue-400 transition-colors"></i>
                                    </div>
                                    <!-- Tooltip (Top) -->
                                    <div class="absolute bottom-full mb-4 left-1/2 -translate-x-1/2 w-48 p-4 rounded-xl bg-neutral-950 border border-white/10 shadow-2xl opacity-0 invisible group-hover/icon:opacity-100 group-hover/icon:visible transition-all duration-300 translate-y-2 group-hover/icon:translate-y-0 z-50 pointer-events-none">
                                        <div class="text-sm font-bold text-white mb-1">Startups</div>
                                        <div class="text-xs text-neutral-400">Times de alto crescimento e escalabilidade.</div>
                                    </div>
                                </div>

                                <!-- 2. Healthcare (Ring 1, Bottom Right) -->
                                <div class="absolute z-20 group/icon cursor-pointer -translate-x-1/2 -translate-y-1/2" style="top: 60%; left: 67.32%;">
                                    <div class="w-12 h-12 rounded-full bg-neutral-900 border border-white/10 flex items-center justify-center shadow-lg group-hover/icon:border-blue-500/50 group-hover/icon:shadow-[0_0_20px_rgba(59,130,246,0.3)] transition-all duration-300 group-hover/icon:scale-110">
                                        <i data-lucide="activity" class="w-5 h-5 text-neutral-400 group-hover/icon:text-blue-400 transition-colors"></i>
                                    </div>
                                    <!-- Tooltip (Right) -->
                                    <div class="absolute left-full ml-4 top-1/2 -translate-y-1/2 w-48 p-4 rounded-xl bg-neutral-950 border border-white/10 shadow-2xl opacity-0 invisible group-hover/icon:opacity-100 group-hover/icon:visible transition-all duration-300 translate-x-2 group-hover/icon:translate-x-0 z-50 pointer-events-none">
                                        <div class="text-sm font-bold text-white mb-1">Healthcare</div>
                                        <div class="text-xs text-neutral-400">Saúde digital, biotecnologia e life sciences.</div>
                                    </div>
                                </div>

                                <!-- 3. Banking (Ring 1, Bottom Left) -->
                                <div class="absolute z-20 group/icon cursor-pointer -translate-x-1/2 -translate-y-1/2" style="top: 60%; left: 32.68%;">
                                    <div class="w-12 h-12 rounded-full bg-neutral-900 border border-white/10 flex items-center justify-center shadow-lg group-hover/icon:border-blue-500/50 group-hover/icon:shadow-[0_0_20px_rgba(59,130,246,0.3)] transition-all duration-300 group-hover/icon:scale-110">
                                        <i data-lucide="landmark" class="w-5 h-5 text-neutral-400 group-hover/icon:text-blue-400 transition-colors"></i>
                                    </div>
                                    <!-- Tooltip (Left) -->
                                    <div class="absolute right-full mr-4 top-1/2 -translate-y-1/2 w-48 p-4 rounded-xl bg-neutral-950 border border-white/10 shadow-2xl opacity-0 invisible group-hover/icon:opacity-100 group-hover/icon:visible transition-all duration-300 -translate-x-2 group-hover/icon:translate-x-0 z-50 pointer-events-none">
                                        <div class="text-sm font-bold text-white mb-1">Banking</div>
                                        <div class="text-xs text-neutral-400">Fintechs, serviços financeiros e pagamentos.</div>
                                    </div>
                                </div>

                                <!-- 4. Technology (Ring 2, Top Right) -->
                                <div class="absolute z-20 group/icon cursor-pointer -translate-x-1/2 -translate-y-1/2" style="top: 32.5%; left: 80.31%;">
                                    <div class="w-12 h-12 rounded-full bg-neutral-900 border border-white/10 flex items-center justify-center shadow-lg group-hover/icon:border-blue-500/50 group-hover/icon:shadow-[0_0_20px_rgba(59,130,246,0.3)] transition-all duration-300 group-hover/icon:scale-110">
                                        <i data-lucide="code-2" class="w-5 h-5 text-neutral-400 group-hover/icon:text-blue-400 transition-colors"></i>
                                    </div>
                                    <!-- Tooltip (Right) -->
                                    <div class="absolute left-full ml-4 top-1/2 -translate-y-1/2 w-48 p-4 rounded-xl bg-neutral-950 border border-white/10 shadow-2xl opacity-0 invisible group-hover/icon:opacity-100 group-hover/icon:visible transition-all duration-300 translate-x-2 group-hover/icon:translate-x-0 z-50 pointer-events-none">
                                        <div class="text-sm font-bold text-white mb-1">Technology & SaaS</div>
                                        <div class="text-xs text-neutral-400">Infraestrutura em nuvem, IA e plataformas.</div>
                                    </div>
                                </div>

                                <!-- 5. Consumer (Ring 2, Bottom) -->
                                <div class="absolute z-20 group/icon cursor-pointer -translate-x-1/2 -translate-y-1/2" style="top: 85%; left: 50%;">
                                    <div class="w-12 h-12 rounded-full bg-neutral-900 border border-white/10 flex items-center justify-center shadow-lg group-hover/icon:border-blue-500/50 group-hover/icon:shadow-[0_0_20px_rgba(59,130,246,0.3)] transition-all duration-300 group-hover/icon:scale-110">
                                        <i data-lucide="shopping-bag" class="w-5 h-5 text-neutral-400 group-hover/icon:text-blue-400 transition-colors"></i>
                                    </div>
                                    <!-- Tooltip (Bottom) -->
                                    <div class="absolute top-full mt-4 left-1/2 -translate-x-1/2 w-48 p-4 rounded-xl bg-neutral-950 border border-white/10 shadow-2xl opacity-0 invisible group-hover/icon:opacity-100 group-hover/icon:visible transition-all duration-300 translate-y-2 group-hover/icon:translate-y-0 z-50 pointer-events-none">
                                        <div class="text-sm font-bold text-white mb-1">Consumer</div>
                                        <div class="text-xs text-neutral-400">Varejo, e-commerce e bens de consumo.</div>
                                    </div>
                                </div>

                                <!-- 6. Industrial (Ring 2, Top Left) -->
                                <div class="absolute z-20 group/icon cursor-pointer -translate-x-1/2 -translate-y-1/2" style="top: 32.5%; left: 19.69%;">
                                    <div class="w-12 h-12 rounded-full bg-neutral-900 border border-white/10 flex items-center justify-center shadow-lg group-hover/icon:border-blue-500/50 group-hover/icon:shadow-[0_0_20px_rgba(59,130,246,0.3)] transition-all duration-300 group-hover/icon:scale-110">
                                        <i data-lucide="factory" class="w-5 h-5 text-neutral-400 group-hover/icon:text-blue-400 transition-colors"></i>
                                    </div>
                                    <!-- Tooltip (Left) -->
                                    <div class="absolute right-full mr-4 top-1/2 -translate-y-1/2 w-48 p-4 rounded-xl bg-neutral-950 border border-white/10 shadow-2xl opacity-0 invisible group-hover/icon:opacity-100 group-hover/icon:visible transition-all duration-300 -translate-x-2 group-hover/icon:translate-x-0 z-50 pointer-events-none">
                                        <div class="text-sm font-bold text-white mb-1">Industrial</div>
                                        <div class="text-xs text-neutral-400">Manufatura avançada e Indústria 4.0.</div>
                                    </div>
                                </div>

                                <!-- 7. Commodities (Ring 3, Top Right) -->
                                <div class="absolute z-20 group/icon cursor-pointer -translate-x-1/2 -translate-y-1/2" style="top: 14.65%; left: 85.35%;">
                                    <div class="w-12 h-12 rounded-full bg-neutral-900 border border-white/10 flex items-center justify-center shadow-lg group-hover/icon:border-blue-500/50 group-hover/icon:shadow-[0_0_20px_rgba(59,130,246,0.3)] transition-all duration-300 group-hover/icon:scale-110">
                                        <i data-lucide="sprout" class="w-5 h-5 text-neutral-400 group-hover/icon:text-blue-400 transition-colors"></i>
                                    </div>
                                    <!-- Tooltip (Right) -->
                                    <div class="absolute left-full ml-4 top-1/2 -translate-y-1/2 w-48 p-4 rounded-xl bg-neutral-950 border border-white/10 shadow-2xl opacity-0 invisible group-hover/icon:opacity-100 group-hover/icon:visible transition-all duration-300 translate-x-2 group-hover/icon:translate-x-0 z-50 pointer-events-none">
                                        <div class="text-sm font-bold text-white mb-1">Commodities</div>
                                        <div class="text-xs text-neutral-400">Agronegócio, trade e logística global.</div>
                                    </div>
                                </div>

                                <!-- 8. Wellness (Ring 3, Bottom Right) -->
                                <div class="absolute z-20 group/icon cursor-pointer -translate-x-1/2 -translate-y-1/2" style="top: 85.35%; left: 85.35%;">
                                    <div class="w-12 h-12 rounded-full bg-neutral-900 border border-white/10 flex items-center justify-center shadow-lg group-hover/icon:border-blue-500/50 group-hover/icon:shadow-[0_0_20px_rgba(59,130,246,0.3)] transition-all duration-300 group-hover/icon:scale-110">
                                        <i data-lucide="heart" class="w-5 h-5 text-neutral-400 group-hover/icon:text-blue-400 transition-colors"></i>
                                    </div>
                                    <!-- Tooltip (Right) -->
                                    <div class="absolute left-full ml-4 top-1/2 -translate-y-1/2 w-48 p-4 rounded-xl bg-neutral-950 border border-white/10 shadow-2xl opacity-0 invisible group-hover/icon:opacity-100 group-hover/icon:visible transition-all duration-300 translate-x-2 group-hover/icon:translate-x-0 z-50 pointer-events-none">
                                        <div class="text-sm font-bold text-white mb-1">Wellness</div>
                                        <div class="text-xs text-neutral-400">Bem-estar corporativo, fitness e healthtechs.</div>
                                    </div>
                                </div>

                                <!-- 9. Media (Ring 3, Bottom Left) -->
                                <div class="absolute z-20 group/icon cursor-pointer -translate-x-1/2 -translate-y-1/2" style="top: 85.35%; left: 14.65%;">
                                    <div class="w-12 h-12 rounded-full bg-neutral-900 border border-white/10 flex items-center justify-center shadow-lg group-hover/icon:border-blue-500/50 group-hover/icon:shadow-[0_0_20px_rgba(59,130,246,0.3)] transition-all duration-300 group-hover/icon:scale-110">
                                        <i data-lucide="gamepad-2" class="w-5 h-5 text-neutral-400 group-hover/icon:text-blue-400 transition-colors"></i>
                                    </div>
                                    <!-- Tooltip (Left) -->
                                    <div class="absolute right-full mr-4 top-1/2 -translate-y-1/2 w-48 p-4 rounded-xl bg-neutral-950 border border-white/10 shadow-2xl opacity-0 invisible group-hover/icon:opacity-100 group-hover/icon:visible transition-all duration-300 -translate-x-2 group-hover/icon:translate-x-0 z-50 pointer-events-none">
                                        <div class="text-sm font-bold text-white mb-1">Media & Gaming</div>
                                        <div class="text-xs text-neutral-400">Entretenimento, e-sports e creator economy.</div>
                                    </div>
                                </div>

                                <!-- 10. Construction (Ring 3, Top Left) -->
                                <div class="absolute z-20 group/icon cursor-pointer -translate-x-1/2 -translate-y-1/2" style="top: 14.65%; left: 14.65%;">
                                    <div class="w-12 h-12 rounded-full bg-neutral-900 border border-white/10 flex items-center justify-center shadow-lg group-hover/icon:border-blue-500/50 group-hover/icon:shadow-[0_0_20px_rgba(59,130,246,0.3)] transition-all duration-300 group-hover/icon:scale-110">
                                        <i data-lucide="hard-hat" class="w-5 h-5 text-neutral-400 group-hover/icon:text-blue-400 transition-colors"></i>
                                    </div>
                                    <!-- Tooltip (Left) -->
                                    <div class="absolute right-full mr-4 top-1/2 -translate-y-1/2 w-48 p-4 rounded-xl bg-neutral-950 border border-white/10 shadow-2xl opacity-0 invisible group-hover/icon:opacity-100 group-hover/icon:visible transition-all duration-300 -translate-x-2 group-hover/icon:translate-x-0 z-50 pointer-events-none">
                                        <div class="text-sm font-bold text-white mb-1">Construction</div>
                                        <div class="text-xs text-neutral-400">Engenharia civil, infraestrutura e energia.</div>
                                    </div>
                                </div>

                            </div>
                        </div>
"""
lines = lines[:527] + [new_content + '\n'] + lines[790:]

with open('/Users/matheussegantine/Desktop/Site Jobler/index2.html', 'w') as f:
    f.writelines(lines)

