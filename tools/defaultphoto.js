    defaultPhoto(brand, model = '') {
      const b = (brand || '').toLowerCase().trim();
      const m = (model || '').toLowerCase().trim();

      // Performance / sport versions (more attractive defaults)
      if (b.includes('bmw') && (m.includes(' m') || m.startsWith('m') || m.includes('m3') || m.includes('m4') || m.includes('m5') || m.includes('m2') || m.includes('x3 m') || m.includes('x5 m'))) {
        return 'https://images.unsplash.com/photo-1555215695-3004980ad54e?w=800&auto=format&fit=crop';
      }
      if ((b.includes('mercedes') || b.includes('mercedes-benz')) && m.includes('amg')) {
        return 'https://images.unsplash.com/photo-1618843479313-40f8afb4b4d8?w=800&auto=format&fit=crop';
      }
      if (b.includes('audi') && (m.includes('rs') || m.includes(' s') || m.includes('s3') || m.includes('s4') || m.includes('s5') || m.includes('rs3') || m.includes('rs6') || m.includes('rs q') || m.includes('sq'))) {
        return 'https://images.unsplash.com/photo-1606664515524-ed2f786a0bd6?w=800&auto=format&fit=crop';
      }
      if ((b.includes('volkswagen') || b === 'vw') && (m.includes('r-line') || m.includes('r line') || m.includes('gti') || m.includes(' r') || m.includes('golf r') || m.includes('polo gti') || m.includes('golf gti'))) {
        if (m.includes('tiguan')) {
          return 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Volkswagen_Tiguan_eTSI_R-Line_%2725_%281%29.jpg/1280px-Volkswagen_Tiguan_eTSI_R-Line_%2725_%281%29.jpg';
        }
        if (m.includes('golf') && m.includes('gti')) {
          return 'https://images.unsplash.com/photo-1541899481282-d53bffe3c35d?w=800&auto=format&fit=crop';
        }
        if (m.includes('polo') && m.includes('gti')) {
          return 'https://images.unsplash.com/photo-1541899481282-d53bffe3c35d?w=800&auto=format&fit=crop';
        }
        return 'https://images.unsplash.com/photo-1541899481282-d53bffe3c35d?w=800&auto=format&fit=crop';
      }
      if (b.includes('cupra') || m.includes('cupra')) {
        return 'https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=800&auto=format&fit=crop';
      }
      if ((b.includes('skoda') || b.includes('škoda')) && (m.includes('vrs') || m.includes('rs') || m.includes('v rs'))) {
        return 'https://images.unsplash.com/photo-1609521263047-f8f205293f24?w=800&auto=format&fit=crop';
      }
      if (b.includes('ford') && (m.includes('st') || m.includes('rs') || m.includes('focus st') || m.includes('fiesta st'))) {
        return 'https://images.unsplash.com/photo-1551830820-330a71b99659?w=800&auto=format&fit=crop';
      }
      if (b.includes('porsche') || m.includes('turbo') || m.includes('gt')) {
        return 'https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=800&auto=format&fit=crop';
      }

      // Specific model overrides
      if ((b.includes('volkswagen') || b === 'vw') && m.includes('tiguan')) {
        return 'https://images.unsplash.com/photo-1541899481282-d53bffe3c35d?w=800&auto=format&fit=crop';
      }

      const photos = {
        bmw: 'https://images.unsplash.com/photo-1555215695-3004980ad54e?w=800&auto=format&fit=crop',
        audi: 'https://images.unsplash.com/photo-1606664515524-ed2f786a0bd6?w=800&auto=format&fit=crop',
        volkswagen: 'https://images.unsplash.com/photo-1541899481282-d53bffe3c35d?w=800&auto=format&fit=crop',
        vw: 'https://images.unsplash.com/photo-1541899481282-d53bffe3c35d?w=800&auto=format&fit=crop',
        mercedes: 'https://images.unsplash.com/photo-1618843479313-40f8afb4b4d8?w=800&auto=format&fit=crop',
        'mercedes-benz': 'https://images.unsplash.com/photo-1618843479313-40f8afb4b4d8?w=800&auto=format&fit=crop',
        toyota: 'https://images.unsplash.com/photo-1621007947382-bb3c3994e3fb?w=800&auto=format&fit=crop',
        skoda: 'https://images.unsplash.com/photo-1609521263047-f8f205293f24?w=800&auto=format&fit=crop',
        škoda: 'https://images.unsplash.com/photo-1609521263047-f8f205293f24?w=800&auto=format&fit=crop',
        renault: 'https://images.unsplash.com/photo-1619767886558-efdc259cde1a?w=800&auto=format&fit=crop',
        peugeot: 'https://images.unsplash.com/photo-1605559424843-9e4c228bf1c2?w=800&auto=format&fit=crop',
        citroen: 'https://images.unsplash.com/photo-1552519507-da3b142c6e3d?w=800&auto=format&fit=crop',
        citroën: 'https://images.unsplash.com/photo-1552519507-da3b142c6e3d?w=800&auto=format&fit=crop',
        opel: 'https://images.unsplash.com/photo-1549317661-bd32c8ce0db2?w=800&auto=format&fit=crop',
        ford: 'https://images.unsplash.com/photo-1551830820-330a71b99659?w=800&auto=format&fit=crop',
        hyundai: 'https://images.unsplash.com/photo-1617531653332-bd46c24f2068?w=800&auto=format&fit=crop',
        kia: 'https://images.unsplash.com/photo-1619767886558-efdc259cde1a?w=800&auto=format&fit=crop',
        mazda: 'https://images.unsplash.com/photo-1617531653332-bd46c24f2068?w=800&auto=format&fit=crop',
        honda: 'https://images.unsplash.com/photo-1605559424843-9e4c228bf1c2?w=800&auto=format&fit=crop',
        fiat: 'https://images.unsplash.com/photo-1552519507-da3b142c6e3d?w=800&auto=format&fit=crop',
        seat: 'https://images.unsplash.com/photo-1541899481282-d53bffe3c35d?w=800&auto=format&fit=crop',
        cupra: 'https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=800&auto=format&fit=crop',
        dacia: 'https://images.unsplash.com/photo-1619767886558-efdc259cde1a?w=800&auto=format&fit=crop',
        nissan: 'https://images.unsplash.com/photo-1621007947382-bb3c3994e3fb?w=800&auto=format&fit=crop',
        volvo: 'https://images.unsplash.com/photo-1618843479313-40f8afb4b4d8?w=800&auto=format&fit=crop',
        porsche: 'https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=800&auto=format&fit=crop',
        tesla: 'https://images.unsplash.com/photo-1560958089-b8a1929cea89?w=800&auto=format&fit=crop',
        alfa: 'https://images.unsplash.com/photo-1555215695-3004980ad54e?w=800&auto=format&fit=crop',
        'alfa romeo': 'https://images.unsplash.com/photo-1555215695-3004980ad54e?w=800&auto=format&fit=crop',
        jaguar: 'https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=800&auto=format&fit=crop',
        landrover: 'https://images.unsplash.com/photo-1519641471654-76ce0107ad1b?w=800&auto=format&fit=crop',
        'land rover': 'https://images.unsplash.com/photo-1519641471654-76ce0107ad1b?w=800&auto=format&fit=crop',
        mini: 'https://images.unsplash.com/photo-1555215695-3004980ad54e?w=800&auto=format&fit=crop',
        suzuki: 'https://images.unsplash.com/photo-1621007947382-bb3c3994e3fb?w=800&auto=format&fit=crop',
        mitsubishi: 'https://images.unsplash.com/photo-1621007947382-bb3c3994e3fb?w=800&auto=format&fit=crop',
        subaru: 'https://images.unsplash.com/photo-1621007947382-bb3c3994e3fb?w=800&auto=format&fit=crop',
        lexus: 'https://images.unsplash.com/photo-1621007947382-bb3c3994e3fb?w=800&auto=format&fit=crop',
        default: 'https://images.unsplash.com/photo-1494976388531-d1058494cdd8?w=800&auto=format&fit=crop'
      };
      return photos[b] || photos.default;
    },
