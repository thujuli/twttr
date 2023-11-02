import { defineStore } from "pinia";
import { ref, computed } from "vue";

export const useAuthStore = defineStore("auth", () => {
  const accessToken = ref(null || localStorage.getItem("accessToken"));
  const refreshToken = ref(null || localStorage.getItem("refreshToken"));
  const userID = ref(null || localStorage.getItem("userID"));

  const isAuthenticated = computed(() => {
    return accessToken.value !== null;
  });

  const setToken = (access_token, refresh_token, user_id) => {
    localStorage.setItem("accessToken", access_token);
    localStorage.setItem("refreshToken", refresh_token);
    localStorage.setItem("userID", user_id);
    accessToken.value = access_token;
    refreshToken.value = refresh_token;
    userID.value = user_id;
  };

  const removeToken = () => {
    localStorage.removeItem("accessToken");
    localStorage.removeItem("refreshToken");
    localStorage.removeItem("userID");
    accessToken.value = null;
    refreshToken.value = null;
    userID.value = null;
  };

  return {
    isAuthenticated,
    setToken,
    removeToken,
    accessToken,
    refreshToken,
    userID,
  };
});
