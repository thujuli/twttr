import { defineStore } from "pinia";
import { ref, computed } from "vue";

export const useAuthStore = defineStore("auth", () => {
  const accessToken = ref(null || localStorage.getItem("accessToken"));
  const refreshToken = ref(null || localStorage.getItem("refreshToken"));

  const isAuthenticated = computed(() => {
    return accessToken.value !== null;
  });

  const setToken = (access_token, refresh_token) => {
    localStorage.setItem("accessToken", access_token);
    localStorage.setItem("refreshToken", refresh_token);
    accessToken.value = access_token;
    refreshToken.value = refresh_token;
  };

  const removeToken = () => {
    localStorage.removeItem("accessToken");
    localStorage.removeItem("refreshToken");
    accessToken.value = null;
    refreshToken.value = null;
  };

  return { isAuthenticated, setToken, removeToken, accessToken, refreshToken };
});
