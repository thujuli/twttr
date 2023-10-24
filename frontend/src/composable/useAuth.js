import axios from "axios";
import { ref } from "vue";

export function useAuth() {
  const tryAuth = async (url, data) => {
    try {
      const response = await axios.post(url, data);
      return response;
    } catch (err) {
      console.log(err.response);
      return err;
    }
  };

  return {
    tryAuth,
  };
}
