using Newtonsoft.Json;
using System;
using System.Net.Http;
using System.Windows.Forms;
using System.Windows.Forms.DataVisualization.Charting;

namespace EkranIothook
{
    public partial class Form3 : Form
    {
        public Form3()
        {
            InitializeComponent();
        }

        private async void button1_Click(object sender, EventArgs e)

        {
            HttpClient httpClient = new HttpClient();

            // HttpRequestMessage oluşturulması
            HttpRequestMessage request = new HttpRequestMessage(HttpMethod.Get, "https://iothook.com/api/device/?api_key=1c1094835fe305ad04096223&results=1");
            request.Headers.Add("api_key", "1c1094835fe305ad04096223");

            HttpResponseMessage response = await httpClient.SendAsync(request);

            var responseString = await response.Content.ReadAsStringAsync();
            var statusCode = response.StatusCode;

            responseString = responseString.Replace("[", "").Replace("]", "");

            IothookMember member = JsonConvert.DeserializeObject<IothookMember>(responseString);
            string field_4 = member.field_4;
            string field_5 = member.field_5;
            string field_6 = member.field_6;

            chart2.Series["Yanma Sayısı"].Points.Add(new DataPoint(0, Convert.ToDouble(field_4)) { AxisLabel = "Kırmızı" });
            chart2.Series["Yanma Sayısı"].Points.Add(new DataPoint(0, Convert.ToDouble(field_5)) { AxisLabel = "Yeşil" });
            chart2.Series["Yanma Sayısı"].Points.Add(new DataPoint(0, Convert.ToDouble(field_6)) { AxisLabel = "Sarı" });
        }
        private async void Form3_Load(object sender, EventArgs e)
        {
            HttpClient httpClient = new HttpClient();

            // HttpRequestMessage oluşturulması
            HttpRequestMessage request = new HttpRequestMessage(HttpMethod.Get, "https://iothook.com/api/device/?api_key=1c1094835fe305ad04096223&results=1");
            request.Headers.Add("api_key", "1c1094835fe305ad04096223");

            HttpResponseMessage response = await httpClient.SendAsync(request);

            var responseString = await response.Content.ReadAsStringAsync();
            var statusCode = response.StatusCode;

            responseString = responseString.Replace("[", "").Replace("]", "");

            IothookMember member = JsonConvert.DeserializeObject<IothookMember>(responseString);
            string field_4 = member.field_4;
            string field_5 = member.field_5;
            string field_6 = member.field_6;

            chartGraph.Series["Yanma Sayısı"].Points.AddXY("Kırmızı", field_4);
            chartGraph.Series["Yanma Sayısı"].Points.AddXY("Yeşil", field_5);
            chartGraph.Series["Yanma Sayısı"].Points.AddXY("Sarı", field_6);

            // MessageBox.Show("Kırmızı: " + field_4 + " Yeşil: " + field_5 + " Sarı: " + field_6);

            // JSON formatına dönüştürülmüş veriyi göster
            //  MessageBox.Show(responseString);
        }

        public class IothookMember
        {
            public string field_4 { get; set; }
            public string field_5 { get; set; }
            public string field_6 { get; set; }
        }

        private async void chart2_Click(object sender, EventArgs e)
        {
            
        }


        //    private async void Form3_Load(object sender, EventArgs e)
        //    {

        //        using (HttpClient httpClient = new HttpClient())
        //        {
        //            try
        //            {
        //                // IoThook API'ye istek gönder
        //                HttpResponseMessage response = await httpClient.GetAsync("https://iothook.com/api/device/?api_key=1c1094835fe305ad04096223&results=2");

        //                // Yanıt başarılı mı kontrol et
        //                if (response.IsSuccessStatusCode)
        //                {
        //                    // JSON veriyi string olarak al
        //                    string responseString = await response.Content.ReadAsStringAsync();

        //                    // JSON veriyi dinamik bir nesneye dönüştür
        //                    dynamic jsonData = JsonConvert.DeserializeObject(responseString);

        //                    // field_1, field_2 ve field_3 değerlerine eriş
        //                    int field4Value = Convert.ToInt32(jsonData.field_4);
        //                    int field5Value = Convert.ToInt32(jsonData.field_5);
        //                    int field6Value = Convert.ToInt32(jsonData.field_6);

        //                    // Ekrana yazdır
        //                    MessageBox.Show($"field_4: {field4Value}, field_5: {field5Value}, field_6: {field6Value}");


        //                    // Chart'e ekleme işlemleri 

        //                    chartGraph.Series["Yanma Sayısı"].Points.Clear();
        //                    chartGraph.Series["Yanma Sayısı"].Points.AddXY("Kırmızı", field4Value);
        //                    chartGraph.Series["Yanma Sayısı"].Points.AddXY("Yeşil", field5Value);
        //                    chartGraph.Series["Yanma Sayısı"].Points.AddXY("Sarı", field6Value);

        //                }
        //                else
        //                {
        //                    MessageBox.Show("HTTP Error: " + response.StatusCode);
        //                }
        //            }
        //            catch (Exception ex)
        //            {
        //                MessageBox.Show("Error: " + ex.Message);
        //            }
        //        }

        //        chartGraph.Series["Yanma Sayısı"].Points.AddXY("Kırmızı", 1);
        //        chartGraph.Series["Yanma Sayısı"].Points.AddXY("Yeşil", 2);
        //        chartGraph.Series["Yanma Sayısı"].Points.AddXY("Sarı", 3);

        //    }
        //}
    }
}
