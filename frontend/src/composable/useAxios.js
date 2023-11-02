import axiosInstance from "../service/axiosInstance";

export function useAxios() {
  const tryFetch = async (url, page, per_page) => {
    try {
      const response = await axiosInstance.get(url, {
        params: {
          page,
          per_page,
        },
      });
      return response;
    } catch (err) {
      return err.response;
    }
  };

  const tryPost = async (url, formData) => {
    try {
      const response = await axiosInstance.post(url, formData, {
        headers: {
          "Content-Type": "application/json",
        },
      });
      return response;
    } catch (err) {
      return err.response;
    }
  };

  const tryUpload = async (url, formData) => {
    try {
      const response = await axiosInstance.post(url, formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });
      return response;
    } catch (err) {
      return err.response;
    }
  };

  const tryLike = async (url) => {
    try {
      const response = await axiosInstance.post(url, null, {
        headers: {
          "Content-Type": "application/json",
        },
      });
      return response;
    } catch (err) {
      return err.response;
    }
  };

  return {
    tryFetch,
    tryPost,
    tryUpload,
    tryLike,
  };
}
