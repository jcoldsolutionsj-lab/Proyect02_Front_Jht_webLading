/**
 * ApiClient - Clase envoltorio para manejar peticiones HTTP centralizadas
 */
class ApiClient {
    static baseUrl = 'http://127.0.0.1:8000'; // Puedes ajustar la URL base aquí

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
        formCotizacion.addEventListener('submit', async (e) => {
            e.preventDefault();

            // Referencias
            const servicio = document.getElementById('cot-servicio').value;
            const nombre = document.getElementById('cot-nombre').value.trim();
            const apellido = document.getElementById('cot-apellido').value.trim();
            const empresa = document.getElementById('cot-empresa').value.trim();
            const correo = document.getElementById('cot-correo').value.trim();
            const celular = document.getElementById('cot-celular').value.trim();

            // Botones
            const btn = document.getElementById('btn-cotizacion');
            const btnContent = document.getElementById('btn-cotizacion-content');
            
            // 1. Validaciones
            if (!servicio || !nombre || !apellido || !correo || !celular) {
                Swal.fire({
                    icon: 'warning',
                    title: 'Campos incompletos',
                    text: 'Por favor, completa todos los campos requeridos.',
                    confirmButtonColor: '#1a1a2e'
                });
                return;
            }

            // Regex de correo (debe contener @ y terminar en .com)
            const emailRegex = /^[^\s@]+@[^\s@]+\.com$/i;
            if (!emailRegex.test(correo)) {
                Swal.fire({
                    icon: 'warning',
                    title: 'Correo inválido',
                    text: 'El correo electrónico debe ser válido y terminar en .com',
                    confirmButtonColor: '#1a1a2e'
                });
                return;
            }

            // Regex de celular (exactamente 9 dígitos)
            const phoneRegex = /^\d{9}$/;
            if (!phoneRegex.test(celular)) {
                Swal.fire({
                    icon: 'warning',
                    title: 'Celular inválido',
                    text: 'El número de celular debe contener exactamente 9 dígitos.',
                    confirmButtonColor: '#1a1a2e'
                });
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

            // Simular un pequeño retardo amigable de 1s para que el usuario perciba que "algo está procesando" (opcional pero pedido: "un spring profesional de demora amigable")
            await new Promise(resolve => setTimeout(resolve, 800));

            // 4. Enviar API
            try {
                await ApiClient.post('/clientes/', payload);
                
                // Success UI
                Swal.fire({
                    icon: 'success',
                    title: '¡Cotización Solicitada!',
                    text: 'Hemos recibido tus datos correctamente. Te contactaremos en menos de 24 horas.',
                    confirmButtonColor: '#d4af37'
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
});
