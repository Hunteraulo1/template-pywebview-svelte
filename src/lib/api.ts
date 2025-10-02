import axios from 'axios';

// Configuration de base d'axios
const api = axios.create({
  baseURL: '/api',
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Types TypeScript pour les réponses API
export interface HealthResponse {
  status: string;
  message: string;
  timestamp: number;
}

// Service API
export const apiService = {
  async healthCheck(): Promise<HealthResponse> {
    const response = await api.get('/health');
    return response.data;
  }
};
