// 리엑트 라이브러리
import React from 'react';
import ReactDOM from 'react-dom/client';

// 우리의 컴포넌트
import './index.css';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
