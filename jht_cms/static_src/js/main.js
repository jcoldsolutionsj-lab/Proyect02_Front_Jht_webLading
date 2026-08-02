document.addEventListener('DOMContentLoaded', () => {
    // 1. Initial Page Load Animation
    document.body.classList.add('fade-in-load');

    // 2. Parallax Effect for Hero Background
    const parallaxBg = document.querySelector('.parallax-bg');
    if (parallaxBg) {
        window.addEventListener('scroll', () => {
            const scrollY = window.scrollY;
            // Moves the background video 15% slower than the foreground
            parallaxBg.style.transform = `translateY(${scrollY * 0.15}px)`;
        }, { passive: true });
    }

    // 3. Scroll-Triggered Animations (Intersection Observer - Repeatable)
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.15 // 15% of the element must be visible
    };

    const scrollObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
            } else {
                entry.target.classList.remove('is-visible');
            }
        });
    }, observerOptions);

    const animatedElements = document.querySelectorAll('.scroll-trigger');
    animatedElements.forEach(el => scrollObserver.observe(el));

    // 5. Slot Machine Counters (Contadores numéricos suaves repetibles)
    const counterObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            const target = entry.target;
            
            if (entry.isIntersecting) {
                const targetValue = parseInt(target.getAttribute('data-counter'), 10);
                const duration = 2000; // 2 segundos (un poco más rápido)
                let startTimestamp = null;

                const step = (timestamp) => {
                    // Prevenir múltiples llamadas superpuestas
                    if (!target.dataset.animating) target.dataset.animating = "true";
                    
                    if (!startTimestamp) startTimestamp = timestamp;
                    const progress = Math.min((timestamp - startTimestamp) / duration, 1);
                    
                    // Curva de aceleración (easeOutExpo)
                    const easeOut = progress === 1 ? 1 : 1 - Math.pow(2, -10 * progress);
                    
                    const currentValue = Math.floor(easeOut * targetValue);
                    target.textContent = currentValue;
                    
                    if (progress < 1) {
                        target.animationFrame = window.requestAnimationFrame(step);
                    } else {
                        target.textContent = targetValue;
                        delete target.dataset.animating;
                    }
                };
                
                // Cancelar cualquier animación previa si entramos rápidamente
                if (target.animationFrame) cancelAnimationFrame(target.animationFrame);
                target.animationFrame = window.requestAnimationFrame(step);
                
            } else {
                // Cuando sale de la pantalla, lo reseteamos a 0 para que vuelva a rodar al entrar
                if (target.animationFrame) cancelAnimationFrame(target.animationFrame);
                delete target.dataset.animating;
                target.textContent = '0';
            }
        });
    }, { threshold: 0.1 });

    document.querySelectorAll('[data-counter]').forEach(counter => {
        counterObserver.observe(counter);
    });
});



// --- SCROLL SUAVE Y LENTO PERSONALIZADO PARA EL MENÚ ---
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                e.preventDefault();
                
                const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset;
                const startPosition = window.pageYOffset;
                const distance = targetPosition - startPosition;
                
                // Duración en milisegundos (1500 = 1.5 segundos, MUY lento y suave)
                const duration = 1500;
                let start = null;
                
                // Función de easing para que arranque y frene muy suave (easeInOutCubic)
                function step(timestamp) {
                    if (!start) start = timestamp;
                    const progress = timestamp - start;
                    let time = progress / duration;
                    if (time > 1) time = 1;
                    
                    const easeInOutCubic = time < 0.5 
                        ? 4 * time * time * time 
                        : 1 - Math.pow(-2 * time + 2, 3) / 2;
                        
                    const currentPosition = startPosition + distance * easeInOutCubic;
                    window.scrollTo(0, currentPosition);
                    
                    if (progress < duration) {
                        window.requestAnimationFrame(step);
                    }
                }
                
                window.requestAnimationFrame(step);
            }
        });
    });
});




/**
 * ApiClient - Clase envoltorio para manejar peticiones HTTP centralizadas
 */
class ApiClient {
    static getBaseUrl() {
        if (window.BACKEND_API_URL) {
            return window.BACKEND_API_URL;
        }
        const hostname = window.location.hostname;
        if (hostname === 'localhost' || hostname === '127.0.0.1' || hostname.startsWith('192.168.')) {
            return `http://${hostname}:8000`;
        }
        return 'https://jht-mnt-api.onrender.com'; // Ajusta esta URL con tu dominio real de Render si es diferente
    }

    static baseUrl = ApiClient.getBaseUrl();

    static async post(endpoint, data, options = {}) {
        const url = `${this.baseUrl}${endpoint}`;
        
        const defaultHeaders = {
            'Content-Type': 'application/json',
            // 'X-CSRFToken': getCookie('csrftoken') // Si se requiere en el futuro
        };

        const config = {
            method: 'POST',
            headers: { ...defaultHeaders, ...options.headers },
            body: JSON.stringify(data),
            ...options
        };

        try {
            const response = await fetch(url, config);
            
            // Tratamos de parsear el JSON, o lanzamos error si la respuesta no es OK
            let responseData;
            const contentType = response.headers.get("content-type");
            if (contentType && contentType.indexOf("application/json") !== -1) {
                responseData = await response.json();
            } else {
                responseData = await response.text();
            }

            if (!response.ok) {
                throw new Error(responseData.detail || responseData.message || 'Error en la petición');
            }

            return responseData;

        } catch (error) {
            console.error(`[ApiClient] Error POST ${endpoint}:`, error);
            throw error;
        }
    }
}

// Lógica de formulario de cotización (Lead Comercial)
document.addEventListener('DOMContentLoaded', () => {
    const formCotizacion = document.getElementById('form-cotizacion');
    
    if (formCotizacion) {
        // Autocompletado de dominios de correo al escribir @
        const emailInput = document.getElementById('cot-correo');
        const emailDatalist = document.getElementById('email-domains');
        if (emailInput && emailDatalist) {
            emailInput.addEventListener('input', () => {
                const val = emailInput.value;
                const atIndex = val.indexOf('@');
                emailDatalist.innerHTML = '';
                if (atIndex !== -1) {
                    const prefix = val.substring(0, atIndex);
                    const domains = ['gmail.com', 'outlook.com', 'hotmail.com', 'yahoo.com', 'coldsolutions.com'];
                    domains.forEach(domain => {
                        const option = document.createElement('option');
                        option.value = `${prefix}@${domain}`;
                        emailDatalist.appendChild(option);
                    });
                }
            });
        }

        formCotizacion.addEventListener('submit', async (e) => {
            e.preventDefault();

            // Referencias de inputs
            const inputServicio = document.getElementById('cot-servicio');
            const inputNombre = document.getElementById('cot-nombre');
            const inputApellido = document.getElementById('cot-apellido');
            const inputEmpresa = document.getElementById('cot-empresa');
            const inputCorreo = document.getElementById('cot-correo');
            const inputCelular = document.getElementById('cot-celular');

            const servicio = inputServicio.value;
            const nombre = inputNombre.value.trim();
            const apellido = inputApellido.value.trim();
            const empresa = inputEmpresa.value.trim();
            const correo = inputCorreo.value.trim();
            const celular = inputCelular.value.trim();

            // Botones
            const btn = document.getElementById('btn-cotizacion');
            const btnContent = document.getElementById('btn-cotizacion-content');
            
            // Helper para limpiar errores previos
            const clearErrors = () => {
                [inputServicio, inputNombre, inputApellido, inputCorreo, inputCelular].forEach(input => {
                    input.classList.remove('border-jht-gold', 'focus:ring-jht-gold', 'ring-1', 'ring-jht-gold');
                });
                ['err-cot-servicio', 'err-cot-nombre', 'err-cot-apellido', 'err-cot-correo', 'err-cot-celular'].forEach(id => {
                    const errSpan = document.getElementById(id);
                    if (errSpan) {
                        errSpan.textContent = '';
                        errSpan.classList.add('hidden');
                    }
                });
            };

            // Helper para mostrar error inline (debajo del input)
            const showError = (inputEl, errSpanId, message) => {
                const errSpan = document.getElementById(errSpanId);
                if (errSpan) {
                    errSpan.textContent = message;
                    errSpan.classList.remove('hidden');
                }
                inputEl.classList.add('border-jht-gold', 'focus:ring-jht-gold', 'ring-1', 'ring-jht-gold');
            };

            clearErrors();
            let isValid = true;

            // 1. Validaciones
            if (!servicio) {
                showError(inputServicio, 'err-cot-servicio', 'Por favor selecciona un servicio.');
                isValid = false;
            }
            if (!nombre) {
                showError(inputNombre, 'err-cot-nombre', 'El nombre es obligatorio.');
                isValid = false;
            }
            if (!apellido) {
                showError(inputApellido, 'err-cot-apellido', 'El apellido es obligatorio.');
                isValid = false;
            }
            
            // Regex de correo (debe contener @ y terminar en .com)
            const emailRegex = /^[^\s@]+@[^\s@]+\.com$/i;
            if (!correo) {
                showError(inputCorreo, 'err-cot-correo', 'El correo electrónico es obligatorio.');
                isValid = false;
            } else if (!emailRegex.test(correo)) {
                showError(inputCorreo, 'err-cot-correo', 'Debe ser un correo válido y terminar en .com (ej. usuario@dominio.com)');
                isValid = false;
            }

            // Regex de celular (9 dígitos locales o 11 dígitos internacionales con 51 al inicio)
            const phoneRegex = /^(?:51)?\d{9}$/;
            if (!celular) {
                showError(inputCelular, 'err-cot-celular', 'El número de celular/teléfono es obligatorio.');
                isValid = false;
            } else if (!phoneRegex.test(celular)) {
                showError(inputCelular, 'err-cot-celular', 'Debe tener 9 dígitos (ej. 945430381 / 012850698) o 11 dígitos (ej. 51945430381).');
                isValid = false;
            }

            if (!isValid) {
                return;
            }

            // 2. Preparar el Payload
            const payload = {
                lea_vservicio: servicio,
                lea_vnombre: nombre,
                lea_vapellido: apellido,
                lea_vcorreo: correo,
                lea_itelefono: parseInt(celular, 10),
                lea_vempresa: empresa || ""
            };

            // 3. UI de Carga (Spinner)
            const originalContent = btnContent.innerHTML;
            btn.disabled = true;
            btnContent.innerHTML = `
                <svg class="animate-spin -ml-1 mr-3 h-5 w-5 text-jht-dark" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                Enviando...
            `;
            btn.classList.add('opacity-80', 'cursor-not-allowed');
            btn.classList.remove('hover:bg-[#d4af37]', 'hover:shadow-xl');

            // 4. Enviar API
            try {
                await ApiClient.post('/clientes/', payload);
                
                // Success UI
                Swal.fire({
                    icon: 'success',
                    title: '¡Cotización Solicitada!',
                    text: `Hemos recibido tus datos correctamente, ${nombre} ${apellido}. Te contactaremos en menos de 24 horas.`,
                    confirmButtonColor: '#d4af37',
                    allowOutsideClick: false
                });
                formCotizacion.reset();

            } catch (error) {
                Swal.fire({
                    icon: 'error',
                    title: 'Hubo un problema',
                    text: 'No pudimos procesar tu solicitud en este momento. Por favor intenta más tarde.',
                    confirmButtonColor: '#d4af37'
                });
            } finally {
                // 5. Restaurar UI
                btn.disabled = false;
                btnContent.innerHTML = originalContent;
                btn.classList.remove('opacity-80', 'cursor-not-allowed');
                btn.classList.add('hover:bg-[#d4af37]', 'hover:shadow-xl');
            }
        });
    }
    // Lógica de formulario Consulta General
    const formContacto = document.getElementById('form-contacto');
    if (formContacto) {
        // Autocompletado de dominios de correo al escribir @
        const emailInputCon = document.getElementById('con-email');
        const emailDatalistCon = document.getElementById('email-domains-contacto');
        if (emailInputCon && emailDatalistCon) {
            emailInputCon.addEventListener('input', () => {
                const val = emailInputCon.value;
                const atIndex = val.indexOf('@');
                emailDatalistCon.innerHTML = '';
                if (atIndex !== -1) {
                    const prefix = val.substring(0, atIndex);
                    const domains = ['gmail.com', 'outlook.com', 'hotmail.com', 'yahoo.com', 'coldsolutions.com'];
                    domains.forEach(domain => {
                        const option = document.createElement('option');
                        option.value = `${prefix}@${domain}`;
                        emailDatalistCon.appendChild(option);
                    });
                }
            });
        }

        // Contador de palabras
        const mensajeInput = document.getElementById('con-mensaje');
        const wordCountSpan = document.getElementById('word-count');
        if (mensajeInput && wordCountSpan) {
            mensajeInput.addEventListener('input', () => {
                const words = mensajeInput.value.trim().split(/\s+/).filter(w => w.length > 0);
                if (words.length > 100) {
                    // Truncar a 100 palabras
                    const truncated = words.slice(0, 100).join(' ');
                    mensajeInput.value = truncated;
                    wordCountSpan.textContent = `100/100 palabras`;
                    wordCountSpan.classList.add('text-jht-gold');
                } else {
                    wordCountSpan.textContent = `${words.length}/100 palabras`;
                    wordCountSpan.classList.remove('text-jht-gold');
                }
            });
        }

        formContacto.addEventListener('submit', async (e) => {
            e.preventDefault();

            const inputNombre = document.getElementById('con-nombre');
            const inputEmail = document.getElementById('con-email');
            const inputTelefono = document.getElementById('con-telefono');
            const inputEmpresa = document.getElementById('con-empresa');
            const inputMensaje = document.getElementById('con-mensaje');

            const nombreCompleto = inputNombre.value.trim();
            const correo = inputEmail.value.trim();
            const celular = inputTelefono.value.trim();
            const empresa = inputEmpresa.value.trim();
            const mensaje = inputMensaje.value.trim();

            const btn = document.getElementById('btn-contacto');
            const btnContent = document.getElementById('btn-contacto-content');

            const clearErrors = () => {
                [inputNombre, inputEmail, inputTelefono, inputMensaje].forEach(input => {
                    if (input) input.classList.remove('border-jht-gold', 'focus:ring-jht-gold', 'ring-1', 'ring-jht-gold');
                });
                ['err-con-nombre', 'err-con-email', 'err-con-telefono', 'err-con-mensaje'].forEach(id => {
                    const errSpan = document.getElementById(id);
                    if (errSpan) {
                        errSpan.textContent = '';
                        errSpan.classList.add('hidden');
                    }
                });
            };

            const showError = (inputEl, errSpanId, message) => {
                const errSpan = document.getElementById(errSpanId);
                if (errSpan) {
                    errSpan.textContent = message;
                    errSpan.classList.remove('hidden');
                }
                if (inputEl) inputEl.classList.add('border-jht-gold', 'focus:ring-jht-gold', 'ring-1', 'ring-jht-gold');
            };

            clearErrors();
            let isValid = true;

            const nameParts = nombreCompleto.split(/\s+/).filter(w => w.length > 0);
            if (nameParts.length < 1) {
                showError(inputNombre, 'err-con-nombre', 'Por favor ingresa tu nombre y apellido.');
                isValid = false;
            } else if (nameParts.length < 2) {
                showError(inputNombre, 'err-con-nombre', 'Por favor ingresa al menos un nombre y un apellido.');
                isValid = false;
            }

            const emailRegex = /^[^\s@]+@[^\s@]+\.com$/i;
            if (!correo) {
                showError(inputEmail, 'err-con-email', 'El correo electrónico es obligatorio.');
                isValid = false;
            } else if (!emailRegex.test(correo)) {
                showError(inputEmail, 'err-con-email', 'Debe ser un correo válido y terminar en .com');
                isValid = false;
            }

            const phoneRegex = /^(?:51)?\d{9}$/;
            if (!celular) {
                showError(inputTelefono, 'err-con-telefono', 'El número de celular/teléfono es obligatorio.');
                isValid = false;
            } else if (!phoneRegex.test(celular)) {
                showError(inputTelefono, 'err-con-telefono', 'Debe tener 9 dígitos o 11 dígitos con 51.');
                isValid = false;
            }

            if (!mensaje) {
                showError(inputMensaje, 'err-con-mensaje', 'Por favor ingresa tu consulta.');
                isValid = false;
            }

            if (!isValid) return;

            const firstName = nameParts[0];
            const lastName = nameParts.slice(1).join(' ');

            const payload = {
                lea_vservicio: mensaje, // Guardar el mensaje en el campo de servicio como solicitaste
                lea_vnombre: firstName,
                lea_vapellido: lastName,
                lea_vcorreo: correo,
                lea_itelefono: parseInt(celular, 10),
                lea_vempresa: empresa || ""
            };

            const originalContent = btnContent.innerHTML;
            btn.disabled = true;
            btnContent.innerHTML = `
                <svg class="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                Enviando...
            `;
            btn.classList.add('opacity-80', 'cursor-not-allowed');

            await new Promise(resolve => setTimeout(resolve, 800));

            try {
                await ApiClient.post('/clientes/', payload);
                
                Swal.fire({
                    icon: 'success',
                    title: '¡Consulta Enviada!',
                    text: `¡Excelente ${firstName}! Hemos recibido tu consulta exitosamente. Sentimos un gran compromiso con nuestros clientes y nos pondremos en contacto contigo a la brevedad posible para brindarte la mejor atención.`,
                    confirmButtonColor: '#d4af37',
                    allowOutsideClick: false
                });
                formContacto.reset();
                if (wordCountSpan) wordCountSpan.textContent = '0/100 palabras';
            } catch (error) {
                Swal.fire({
                    icon: 'error',
                    title: 'Hubo un problema',
                    text: 'No pudimos procesar tu solicitud. Por favor intenta más tarde.',
                    confirmButtonColor: '#d4af37'
                });
            } finally {
                btn.disabled = false;
                btn.classList.remove('opacity-80', 'cursor-not-allowed');
                btnContent.innerHTML = originalContent;
            }
        });
    }
});
