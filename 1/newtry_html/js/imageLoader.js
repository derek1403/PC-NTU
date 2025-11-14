/**
 * 颱風圖片載入模組
 * 負責從 Digital Typhoon 載入衛星圖片
 */

/**
 * 生成可能的 TC ID 候選列表
 * @param {string} tcId - 原始 TC ID
 * @returns {Array<string>} 候選 TC ID 列表
 */
function generateTcIdCandidates(tcId) {
  const tcIdNum = tcId.slice(0, -1);
  const year = tcIdNum.slice(0, 4);
  const num = parseInt(tcIdNum.slice(4));
  const candidates = [];
  
  for (let i = 0; i < 7; i++) {
    const tryNum = num - i;
    if (tryNum < 1) break;
    const tryTcId = `${year}${String(tryNum).padStart(2, '0')}`;
    candidates.push(tryTcId);
  }
  
  return candidates;
}

/**
 * 載入單張颱風圖片
 * @param {string} tcId - 颱風編號
 * @param {string} time - 時間
 * @param {number} order - 順序
 * @returns {Promise<HTMLImageElement|null>} 圖片元素或 null
 */
export function loadTyphoonImage(tcId, time, order) {
  return new Promise((resolve) => {
    const tcIdCandidates = generateTcIdCandidates(tcId);
    const allCandidates = [];
    
    // 如果是202524W(RAGASA) 因為輸入的檔案在2025年只有RAGASA這個颱風，可以直接給定
    if (tcId === '202524'){
      console.log('📌 IS RAGASA');
      allCandidates.push(
        `https://agora.ex.nii.ac.jp/digital-typhoon/wnp/by-name/202518/4/512x512/HMW9${time.slice(2)}.202518.jpg`
      );
    } else{
      for (const tryTcId of tcIdCandidates) {
        allCandidates.push(
          `https://agora.ex.nii.ac.jp/digital-typhoon/wnp/by-name/${tryTcId}/4/512x512/MTS1${time.slice(2)}.${tryTcId}.jpg`,
          `https://agora.ex.nii.ac.jp/digital-typhoon/wnp/by-name/${tryTcId}/4/512x512/MTS2${time.slice(2)}.${tryTcId}.jpg`,
          `https://agora.ex.nii.ac.jp/digital-typhoon/wnp/by-name/${tryTcId}/3/512x512/GOE9${time.slice(2)}.${tryTcId}.jpg`,
          `https://agora.ex.nii.ac.jp/digital-typhoon/wnp/by-name/${tryTcId}/1/512x512/GMS1${time.slice(2)}.${tryTcId}.jpg`,
          `https://agora.ex.nii.ac.jp/digital-typhoon/wnp/by-name/${tryTcId}/1/512x512/GMS2${time.slice(2)}.${tryTcId}.jpg`,
          `https://agora.ex.nii.ac.jp/digital-typhoon/wnp/by-name/${tryTcId}/1/512x512/GMS3${time.slice(2)}.${tryTcId}.jpg`,
          `https://agora.ex.nii.ac.jp/digital-typhoon/wnp/by-name/${tryTcId}/1/512x512/GMS4${time.slice(2)}.${tryTcId}.jpg`,
          `https://agora.ex.nii.ac.jp/digital-typhoon/wnp/by-name/${tryTcId}/3/512x512/GMS5${time.slice(2)}.${tryTcId}.jpg`,
          `https://agora.ex.nii.ac.jp/digital-typhoon/wnp/by-name/${tryTcId}/4/512x512/HMW8${time.slice(2)}.${tryTcId}.jpg`,
          `https://agora.ex.nii.ac.jp/digital-typhoon/wnp/by-name/${tryTcId}/4/512x512/HMW9${time.slice(2)}.${tryTcId}.jpg`
        );
      }
    }
    // 建立所有可能的圖片 URL 因為沒有JTWC和JMA的兌換表

    
    // 備用圖片
    allCandidates.push(
      `https://media.istockphoto.com/id/1503385646/zh/%E7%85%A7%E7%89%87/portrait-funny-and-happy-shiba-inu-puppy-dog-peeking-out-from-behind-a-blue-banner-isolated-on.jpg?s=612x612&w=0&k=20&c=j6W1QMERTVgCfKQq7aWLv4m4vUmzHEaC8Iul9883-iE=`
    );

    const img = document.createElement('img');
    img.alt = `颱風 ${tcId} 圖片`;
    img.style.maxWidth = "100%";
    img.style.borderRadius = "8px";
    img.style.boxShadow = "0 2px 8px rgba(0,0,0,0.15)";

    let currentIndex = 0;

    function tryLoadImage() {
      if (currentIndex >= allCandidates.length) {
        resolve(null);
        return;
      }

      const currentUrl = allCandidates[currentIndex];
      img.src = currentUrl;

      img.onload = function() {
        resolve(img);
      };

      img.onerror = function() {
        currentIndex++;
        tryLoadImage();
      };
    }

    tryLoadImage();
  });
}

/**
 * 載入多張颱風圖片
 * @param {Array<string>} tcIds - 颱風編號陣列
 * @param {Array<string>} times - 時間陣列
 * @param {Array<number>} orders - 順序陣列
 * @param {HTMLElement} container - 容器元素
 */
export async function loadMultipleTyphoonImages(tcIds, times, orders, container) {
  container.innerHTML = '<div class="image-loading">🖼️ 載入圖片中...</div>';

  const maxImages = 5;
  const imagePromises = [];

  // 只處理西北太平洋颱風
  for (let i = 0; i < tcIds.length; i++) {
    const tcId = String(tcIds[i]);
    
    if (["K", "W"].includes(tcId.slice(-1))) {
      imagePromises.push(
        loadTyphoonImage(tcId, String(times[i]), orders[i])
      );
    }

    if (imagePromises.length >= maxImages) {
      break;
    }
  }

  if (imagePromises.length === 0) {
    container.innerHTML = '<div class="image-loading" style="color: #999;">⚠️ 無西北太平洋颱風圖片</div>';
    return;
  }

  const images = await Promise.all(imagePromises);
  container.innerHTML = '';

  let successCount = 0;
  images.forEach((img, index) => {
    if (img) {
      const wrapper = document.createElement('div');
      wrapper.className = 'image-wrapper';
      
      wrapper.appendChild(img);
      
      const caption = document.createElement('div');
      caption.className = 'image-caption';
      
      // 找到對應的原始索引
      let originalIndex = 0;
      let validCount = 0;
      for (let j = 0; j < tcIds.length; j++) {
        if (["K", "W"].includes(String(tcIds[j]).slice(-1))) {
          if (validCount === index) {
            originalIndex = j;
            break;
          }
          validCount++;
        }
      }
      
      caption.textContent = `颱風 ${tcIds[originalIndex]} - ${times[originalIndex]}`;
      wrapper.appendChild(caption);
      
      container.appendChild(wrapper);
      successCount++;
    }
  });

  if (successCount === 0) {
    container.innerHTML = '<div class="image-loading" style="color: #999;">⚠️ 無可用圖片</div>';
  }
}