import axios from "axios";

export function useAuth() {
  const tryAuth = async (url, formData) => {
    try {
      const response = await axios.post(url, formData);
      return response;
    } catch (err) {
      return err.response;
    }
  };

  const tryLogout = async (url, access_token) => {
    try {
      const response = await axios.delete(url, {
        headers: {
          "Content-Type": "application/json",
          Authorization: "Bearer " + access_token,
        },
      });
      return response;
    } catch (err) {
      return err.response;
    }
  };

  return {
    tryAuth,
    tryLogout,
  };
}
